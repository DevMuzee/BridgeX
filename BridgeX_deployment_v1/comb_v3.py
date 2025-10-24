import pandas as pd
import requests
import sqlite3
from sqlalchemy import create_engine


class APIClient:
    """API integration testing pull begin"""
    def __init__(self, api_url):
        self.api_url= api_url

    def fetch_user_data(self):

        try:
            response= requests.get(self.api_url, timeout=10)
            if response.status_code== 200:

                data=response.json()
                df= pd.json_normalize(data)
                return df
            else: 
                raise Exception("API request failed with status code {response.status_code}") 
        except requests.exceptions.RequestException as e:
            raise Exception(f'API connection failed {e}')
    


class PostgreConnect:
    """PostgreSQL connection base establishment"""
    def __init__(self, user, password, host, port, db_name):
        self.user= user
        self.password= password
        self.host= host
        self.port = port
        self.db_name= db_name

        #create connection engine
        self.engine= create_engine( f"postgresql://{user}:{password}@{host}:{port}/{db_name}")

    def api_postgre_save(self, data_frame, table_name="api_data"):
        """Save API data to PostgreSQL database"""
        try:
            data_frame.to_sql(table_name, self.engine, if_exists= 'replace', index= False)
            print(f'✅ Data has succesfully been saved to PostgreSQL table {table_name}')
        except Exception as e:
            print(f"❌ Error saving data: {e}")


class DatabaseConnect:
    """Using sqlite3 database"""
    def __init__(self, db_name= "local_repo.db"):
        self.db_name= db_name
        # self._create_table()

    def api_data_save(self, data_frame, table_name= "api_data"):
        """Saving API data to SQLite database"""
        conn= sqlite3.connect(self.db_name)
        data_frame.to_sql(table_name, conn, if_exists= 'replace', index=False)
        conn.close()



def get_postgresql_connection():
    """Prompt user for PostgreSQL connection details and return an object."""
    print("\n--- PostgreSQL Connection Setup ---")
    user= input("Enter PostgreSQL username: ").strip()
    password= input("Enter PostgreSQL password: ").strip()
    host= input("Enter PostgreSQL host (e.g., localhost or remote IP): ").strip()
    port= input('Enter PostgreSQL port (default 5432): ').strip() or "5432"
    db_name= input("Enter PostgreSQL database name: ").strip()
    table_name= input('Enter PostgreSQL table name: ').strip() or "api_data"

    return user, password, host, port, db_name, table_name


def main():
    print("--- BridgeX API to PostgreSQL ---")
    api_url= input("Enter your API url: ").strip()
    api_client= APIClient(api_url)

    #Fetch data from API
    df= api_client.fetch_user_data()
    print(f"\n✅ API Data fetched successfully with {len(df)} records.\n")

    while True:
        #Choose where to save
        print("Where would you like to save your data?")
        print("1️ SQLite3 Database")
        print("2️ PostgreSQL Database")
        print("3️ Both")
        print("🔚 type 'exit' to quit")

        choice = input("Enter your choice (1/2/3 or 'exit'): ").strip().lower()

        if choice == "1":
            db_client=DatabaseConnect()
            db_client.api_data_save(df)
            #print(df.columns)

        elif choice == "2":
            user, password, host, port, db_name, table_name = get_postgresql_connection()
            pg_client= PostgreConnect(user, password, host, port, db_name)
            pg_client.api_postgre_save(df, table_name)

        elif choice == "3":
            db_client=DatabaseConnect()
            db_client.api_data_save(df, table_name)
            user, password, host, port, db_name, table_name = get_postgresql_connection()
            pg_client= PostgreConnect(user, password, host, port, db_name)
            pg_client.api_postgre_save(df, table_name)
        
        elif choice == 'exit':
            print("\n👋 Exiting program. Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3 or type 'exit' to quit.")
            continue #loop again for valid input

        print("\n✅ Operation completed successfully!")
        break

if __name__== "__main__":
    main()













# class RequestGet:
#     def __init__(self, api_client, db_client):
#         self.api_client= api_client
#         self.db_client= db_client

#     def api_get_data(self):
#         """Integrating data from API_repo to database"""
#         api_repo= self.api_client.fetch_user_data()
#         self.db_client.api_data_save(api_repo)
#         return api_repo.head()
    
#     def postgre_get_data(self):
#         """Integrating for PostgreSQL data fetch"""
#         repo_api= self.api_client.fetch_user_data()
#         self.db_client.api_postgre_save(repo_api)
#         return repo_api.head()


"""Displaying the gotten api result from the database"""
# api_client = APIClient(api_url="https://jsonplaceholder.typicode.com/users")
# db_client= DatabaseConnect("remote_repo.db")
# servers= RequestGet(api_client, db_client) 

# df= servers.api_get_data()

# print("API data:", api_client)
# print("DB data:", db_client)
# print('Logging into server.........')
# pd.set_option('display.max.columns', 4)
# print(df.head())

