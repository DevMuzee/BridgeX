import pandas as pd
import os
import sqlite3

class LocalRepo:
    """Class to handle local CSV repository operations"""

    def __init__(self, file_path= "C:/Users/abdulmuiz.adewale/OneDrive - Tolaram Pte Ltd/Project Done/BorderX ETL_pipeline/Online Retail.xlsx"):
        """Change the file path to the file name path"""
        self.file_path= file_path

    def read_data(self):
        """Reading data from local CSV file"""
        if os.path.exists(self.file_path):
            data= pd.read_excel(self.file_path)
            return data
        raise FileNotFoundError("The specified file does not exist")



class DatabaseClient:
    def __init__(self, db_name= "local_database.db"):
        self.db_name= db_name

    def save_data(self, data_frame, table_name= "online_retail"):
        """Saving local data to SQLite database"""
        conn= sqlite3.connect(self.db_name)
        data_frame.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()


class DataIntegrator:
    def __init__(self, repo_client, db_client):
        self.repo_client= repo_client
        self.db_client= db_client

    def integrate_data(self):
        """Integrating data from local repository to database"""
        data= self.repo_client.read_data()
        self.db_client.save_data(data)
        return data.head()

#checking if the database was created
local_repo= LocalRepo()
db_client= DatabaseClient("local_database.db")
server= DataIntegrator(local_repo, db_client)

df= server.integrate_data()
# print(df.head())
