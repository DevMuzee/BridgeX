from api_intg import APIClient, DatabaseConnect, RequestGet
import pytest
import pandas as pd

def test_integration_with_jsonplaceholder():
    api_get= APIClient("https://jsonplaceholder.typicode.com/users")
    db_connect= DatabaseConnect('test_users.db')
    server= RequestGet(api_get, db_connect)

    df= server.api_get_data()

    #assering the db its a dataframe
    assert isinstance(df, pd.DataFrame)
    #assert isinstance(df, list)
    
    # assert not df.empty()
    assert len(df) > 0

    #checking field in the first record
    first = df.columns
    assert "username" in first or "name" in first
    assert "email" in first


#checking if the fetched API data is what is stored in the DB
def test_api_to_db():
    api_client = APIClient(api_url="https://jsonplaceholder.typicode.com/users")
    db_client= DatabaseConnect("test_users.db")
    servers= RequestGet(api_client, db_client)

    #api fetch
    api_fetch= api_client.fetch_user_data()
    db_client.api_data_save(api_fetch)

    #fetching the data back from DB
    db_get = servers.api_get_data()
    # db_get= [dict(zip(key, row)) for row in db_row]

    #logging in
    print("API data:", api_fetch)
    print("DB data:", db_get)

    #assertation
    assert db_get.to_dict(orient= "records") == api_fetch.to_dict(orient="records"), "Mismatch between API-fetched data and DB-saved data" 

    