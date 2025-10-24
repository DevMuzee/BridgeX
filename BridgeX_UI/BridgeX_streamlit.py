import pandas as pd
import requests
import sqlite3
from sqlalchemy import create_engine
import streamlit as st

# ---------- CLASSES ----------

class APIClient:
    """Fetch and normalize data from an API."""
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_user_data(self):
        """Fetch data from API and return as Pandas DataFrame."""
        try:
            response = requests.get(self.api_url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                df = pd.json_normalize(data)
                return df
            else:
                st.error(f"❌ API request failed with status code {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            st.error(f"❌ API connection failed: {e}")
            return None


class PostgreConnect:
    """Handle PostgreSQL database connections and saving."""
    def __init__(self, user, password, host, port, db_name):
        self.engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{db_name}")

    def save_to_postgre(self, data_frame, table_name):
        """Save DataFrame to PostgreSQL."""
        try:
            data_frame.to_sql(table_name, self.engine, if_exists="replace", index=False)
            st.success(f"✅ Data saved to PostgreSQL table '{table_name}' successfully!")
        except Exception as e:
            st.error(f"❌ Error saving to PostgreSQL: {e}")


class SQLiteConnect:
    """Handle SQLite database connections and saving."""
    def __init__(self, db_name="local_repo.db"):
        self.db_name = db_name

    def save_to_sqlite(self, data_frame, table_name):
        """Save DataFrame to SQLite."""
        try:
            conn = sqlite3.connect(self.db_name)
            data_frame.to_sql(table_name, conn, if_exists="replace", index=False)
            conn.close()
            st.success(f"✅ Data saved to SQLite table '{table_name}' successfully!")
        except Exception as e:
            st.error(f"❌ Error saving to SQLite: {e}")

# ---------- STREAMLIT UI ----------

st.set_page_config(page_title="BridgeX API Integration", page_icon="🌉", layout="centered")

st.title("🌉 BridgeX API to Database Integration")
st.write("Easily fetch API data and store it in SQLite or PostgreSQL — now through a web-based interface!")

# Step 1: API Input
st.subheader("🔗 Step 1: Enter API URL")
api_url = st.text_input("Enter your API URL:", "https://jsonplaceholder.typicode.com/users")

if st.button("Fetch API Data"):
    api_client = APIClient(api_url)
    df = api_client.fetch_user_data()
    if df is not None:
        st.success("✅ Data fetched successfully!")
        st.dataframe(df.head())
        st.session_state["api_data"] = df
    else:
        st.error("Failed to fetch data. Please check your API URL.")

# Step 2: Database Selection
if "api_data" in st.session_state:
    st.subheader("💾 Step 2: Choose Where to Save Data")
    db_choice = st.radio(
        "Select database:",
        ["SQLite", "PostgreSQL", "Both"]
    )

    table_name = st.text_input("Enter table name:", "api_data")

    if db_choice in ["PostgreSQL", "Both"]:
        st.markdown("#### 🐘 PostgreSQL Connection Details")
        user = st.text_input("Username")
        password = st.text_input("Password", type="password")
        host = st.text_input("Host", "localhost")
        port = st.text_input("Port", "5432")
        db_name = st.text_input("Database name")

    if st.button("Save Data"):
        df = st.session_state["api_data"]

        if db_choice == "SQLite":
            sqlite_conn = SQLiteConnect()
            sqlite_conn.save_to_sqlite(df, table_name)

        elif db_choice == "PostgreSQL":
            if all([user, password, host, port, db_name]):
                pg_conn = PostgreConnect(user, password, host, port, db_name)
                pg_conn.save_to_postgre(df, table_name)
            else:
                st.error("Please fill in all PostgreSQL connection fields.")

        elif db_choice == "Both":
            sqlite_conn = SQLiteConnect()
            sqlite_conn.save_to_sqlite(df, table_name)

            if all([user, password, host, port, db_name]):
                pg_conn = PostgreConnect(user, password, host, port, db_name)
                pg_conn.save_to_postgre(df, table_name)
            else:
                st.error("Please fill in all PostgreSQL connection fields.")
