import pandas as pd
from sqlalchemy import create_engine
import requests

def get_postgresql_connection():
    print("\n--- PostgreSQL Connection Setup ---")
    user= input("Enter PostgreSQL username: ").strip()
    password= input("Enter PostgreSQL password: ").strip()
    host= input("Enter PostgreSQL host (e.g., localhost or remote IP): ").strip()
    port= input('Enter PostgreSQL port (default 5432): ').strip() or "5432"
    db_name= input("Enter PostgreSQL database name: ").strip()

    #creating the connection string
    conn_str= f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
    print(f"\n✅ Connection string created: {conn_str}\n")
    return conn_str

def main():
    print("--- BridgeX API to PostgreSQL ---")
    api_url= input("Enter your API url: ").strip()

    # fetch API data
    response= requests.get(api_url)
    if response.status_code== 200:
        data= response.json()
        df= pd.json_normalize(data)
    
    # Get postgreSQL connection info
    pg_conn_str= get_postgresql_connection()
    engine= create_engine(pg_conn_str)

    #creating a table name for the data
    table_name= input('Enter PostgreSQL table name: ').strip() or "api_data"
    df.to_sql(table_name, engine, if_exists="replace", index= False)

    print(f"✅ Data successfully saved to table '{table_name}' in PostgreSQL database.")

if __name__== "__main__":
    main()
