
# BRIX — BRidge Integration eXecutor (BridgeX Phase 6)

**Short name:** BRIX  
**Project:** BridgeX / BRIX — Phase 6 (Streamlit UI)  
**Author / Developer:** Adewale Abdulmuiz Akorede  
**Contact:** adewaleabdulmuiz75@gmail.com

---

## Project Overview
BRIX (BRidge Integration eXecutor) is the Streamlit-enabled user interface for the BridgeX project. It converts the existing command-line API ingestion and database storage pipeline into a clean, user-friendly web application. The app enables users to:
- Enter an API URL
- Preview normalized API responses as a table
- Choose to store results in **SQLite**, **PostgreSQL**, or **Both**
- Supply PostgreSQL credentials securely (locally) and save data with a single click

BRIX emphasizes **Execution**, **Simplicity**, and **Adoption** — making integration tasks easy to run, simple to understand, and practical enough to be adopted by users.

---

## Key Features
- Interactive browser interface (no command-line required)
- API fetch and JSON normalization via `pandas.json_normalize`
- Save to local SQLite (auto-created) or remote PostgreSQL (via SQLAlchemy)
- Input validation and user feedback (success / error messages)
- Session-state management for fetched data preview
- Minimal external dependencies for easy deployment

---

## Technologies & Libraries
- Python 3.8+
- streamlit
- pandas
- requests
- sqlalchemy
- psycopg2-binary (PostgreSQL driver)
- sqlite3 (Python stdlib)

---

## Installation & Setup

1. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\Scripts\activate    # Windows (PowerShell)
   ```

2. Install the required packages:
   ```bash
   pip install streamlit pandas requests sqlalchemy psycopg2-binary
   ```

> Note: On Windows, `psycopg2-binary` typically works out of the box. On Linux/macOS, you may need system packages (e.g., `libpq-dev`) before installing `psycopg2-binary`.

---

## Usage (Run the Streamlit App)

1. Save the Streamlit app file `BridgeX_streamlit.py` (included below).
2. Run the app:
   ```bash
   streamlit run BridgeX_streamlit.py
   ```
3. Your browser will open the BRIX interface. Follow these steps in the UI:
   - Enter your API URL and click **Fetch API Data**
   - Preview the data table
   - Choose a storage option: **SQLite**, **PostgreSQL**, or **Both**
   - If PostgreSQL is chosen, provide credentials (username, password, host, port, db name)
   - Click **Save Data** to persist

---

## PART Streamlit App Code (BridgeX_streamlit.py)

```python

# ---------- STREAMLIT UI ----------

st.set_page_config(page_title="BRIX — Bridge Integration eXecutor", page_icon="🌉", layout="centered")
st.title("BRIX — Bridge Integration eXecutor")
st.write("Fetch API data and save to SQLite or PostgreSQL — a simple, production-minded interface.")

st.markdown("---")
st.subheader("Step 1: Enter API URL")
api_url = st.text_input("API URL", "https://jsonplaceholder.typicode.com/users")

if st.button("Fetch API Data"):
    if not api_url:
        st.error("Please enter a valid API URL.")
    else:
        api_client = APIClient(api_url)
        df = api_client.fetch_user_data()
        if df is not None and not df.empty:
            st.session_state['api_data'] = df
            st.success(f"Fetched {len(df)} records.")
            st.dataframe(df.head())
        else:
            st.error("No data returned or failed to fetch.")

if 'api_data' in st.session_state:
    st.markdown("---")
    st.subheader("Step 2: Choose Storage Option")
    db_choice = st.radio("Save to:", ("SQLite", "PostgreSQL", "Both"))
    table_name = st.text_input("Table name", "api_data")

    if db_choice in ("PostgreSQL", "Both"):
        st.markdown("#### PostgreSQL connection details") 
        col1, col2 = st.columns(2)
        with col1:
            user = st.text_input("Username", value="")
            host = st.text_input("Host", value="localhost")
            db_name = st.text_input("Database name", value="")
        with col2:
            password = st.text_input("Password", type="password")
            port = st.text_input("Port", value="5432")

    if st.button("Save Data"):
        df = st.session_state['api_data']

        if db_choice == "SQLite":
            sqlite_conn = SQLiteConnect()
            sqlite_conn.save_to_sqlite(df, table_name)

        elif db_choice == "PostgreSQL":
            if not all([user, password, host, port, db_name]):
                st.error("Please fill all PostgreSQL connection fields.")
            else:
                pg = PostgreConnect(user, password, host, port, db_name)
                pg.save_to_postgre(df, table_name)

        elif db_choice == "Both":
            sqlite_conn = SQLiteConnect()
            sqlite_conn.save_to_sqlite(df, table_name)

            if not all([user, password, host, port, db_name]):
                st.error("Please fill all PostgreSQL connection fields to save to PostgreSQL.")
            else:
                pg = PostgreConnect(user, password, host, port, db_name)
                pg.save_to_postgre(df, table_name)

st.markdown("---")
st.caption("BRIX — Built for Execution · Simplicity · Adoption")
```

---

## Security & Practical Notes
- **Credentials:** Streamlit apps running locally store inputs in memory only; avoid deploying this exact app without adding secure secret management. Use environment variables or Streamlit's Secrets Manager for production.  
- **SQL Injection / Safety:** This app uses Pandas' `to_sql()` which handles parameterization; however, validate table names in production.  
- **Large Data:** For very large responses, consider chunking or streaming approaches and avoid loading extremely large payloads into memory.

---

## Deployment Suggestions
- **Local testing:** `streamlit run BridgeX_streamlit.py`
- **Cloud deployment:** Streamlit Cloud, Heroku, Render, or a Docker container with environment variables for secrets.

---

## License
MIT License — feel free to reuse and adapt for educational or portfolio purposes.

---

## Contact
**Adewale Abdulmuiz Akorede**  
Email: adewaleabdulmuiz75@gmail.com  
LinkedIn: https://www.linkedin.com/in/abdulmuiz-akorede

