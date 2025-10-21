from integration_p1 import LocalRepo, DatabaseClient, DataIntegrator
import pytest
import pandas as pd

# def test_integration_data(mocker):
#     """testing DataIntegrator with mocked APIClient and DatabaseClient"""
#     mock_api_client= mocker.Mock(LocalRepo)
#     mock_dbi_client= mocker.Mock(DatabaseClient)

#     """Workign on the returning value for each function of the mocked class"""
#     data= mock_api_client.read_data.return_value 
#     data_frame =mock_dbi_client.save_data.return_value

#     """creating UserServices instance with the mocked clients"""
#     integrator= DataIntegrator(mock_api_client, mock_dbi_client)
#     df= integrator.integrate_data(data)

#     """asserting the mocked values"""
#     assert df == data
#     assert data_frame == data
#     mock_api_client.read_data.assert_called_once_with()
#     mock_dbi_client.save_data.assert_called_once_with()


#live testing integration
def test_integrate_data_integrator(): 
    """Integration test for DataIntegrator with real LocalRepo and DatabaseClient"""
    local_repo= LocalRepo()
    db_client= DatabaseClient("test_local_database.db")
    server= DataIntegrator(local_repo, db_client)

    df= server.integrate_data()

    #asserting it returns a dataframe
    assert isinstance(df, pd.DataFrame)
    
    #assert the dataframe is not empty
    assert not df.empty

    #asserting the expected column are returned
    expected_cols= ['InvoiceNo', 'StockCode', 'Description']

    assert all(col in df.columns for col in expected_cols)
