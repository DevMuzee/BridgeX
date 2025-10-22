import pandas as pd
import requests
import sqlite3
from sqlalchemy import create_engine


class APIClient:
    """API integration testing pull begin"""
    def __init__(self, api_url= "https://jsonplaceholder.typicode.com/users"):
        self.api_url= api_url

    def fetch_user_data(self):

        try:
            response= requests.get(self.api_url, timeout=10)
            if response.status_code== 200:

                data=response.json()
                df= pd.json_normalize(data)
                return df
            
        except requests.exceptions.RequestException as e:
            raise Exception(f'API connection failed {e}')
    


class PostgreConnect:
    """PostgreSQL connection base establishment"""
    def __init__(self, user, passw, host, port, db_name):
        self.user= user
        self.passw= passw
        self.host= host
        self.port = port
        self.db_name= db_name

        #create connection engine
        self.engine= create_engine( f"postgresql://{user}:{passw}@{host}:{port}/{db_name}")

    def api_postgre_save(self, data_frame, table_name= 'users_postgre.db'):
        """Save API data to PostgreSQL database"""
        try:
            data_frame.to_sql(table_name, self.engine, if_exists= 'replace', index= False)
            print(f'✅ Data has succesfully been saved to PostgreSQL table {table_name}')
        except Exception as e:
            print(f"❌ Error saving data: {e}")


class DatabaseConnect:
    """Using sqlite3 database"""
    def __init__(self, db_name= 'remote_repo.db'):
        self.db_name= db_name
        # self._create_table()

    def api_data_save(self, data_frame, table_name= 'users_api'):
        """Saving API data to SQLite database"""
        conn= sqlite3.connect(self.db_name)
        data_frame.to_sql(table_name, conn, if_exists= 'replace', index=False)
        conn.close()


class RequestGet:
    def __init__(self, api_client, db_client):
        self.api_client= api_client
        self.db_client= db_client

    def api_get_data(self):
        """Integrating data from API_repo to database"""
        api_repo= self.api_client.fetch_user_data()
        self.db_client.api_data_save(api_repo)
        return api_repo.head()
    
    def postgre_get_data(self):
        """Integrating for PostgreSQL data fetch"""
        repo_api= self.api_client.fetch_user_data()
        self.db_client.api_postgre_save(repo_api)
        return repo_api.head()


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

