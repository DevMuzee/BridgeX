from rev import APIClient, UserServices, DatabaseClient
import pytest

#preparing the mocks
def test_register_user(mocker):
    """testing UserServices with mocked APIClient and DatabaseClient"""
    mock_api_client= mocker.Mock(spec= APIClient)
    mock_db_client= mocker.Mock(spec= DatabaseClient)

    """setting return values for the mocked methods"""
    mock_api_client.get_user_data.return_value= {
        'username': 'ibrahim sulaimon',
        'email': 'ibrahimsulaimon@gmail.com',
        'age': 0
    }
    mock_db_client.save_user.return_value= {
        'username': 'ibrahim sulaimon',
        'email': 'ibrahimsulaimon@gmail.com',
        'age': 0
    }

    """creating UserServices instance with the mocked clients"""
    services= UserServices(mock_api_client, mock_db_client)
    """calling the register_user method"""
    result= services.register_user('ibrahim sulaimon', 'ibrahimsulaimon@gmail.com', 0)

    #assertations
    """checking the result and that the mocked methods were called correctly"""
    assert result == ('IBRAHIM SULAIMON')
    mock_api_client.get_user_data.assert_called_once_with('ibrahim sulaimon','ibrahimsulaimon@gmail.com', 0)
    mock_db_client.save_user.assert_called_once_with('ibrahim sulaimon','ibrahimsulaimon@gmail.com', 0)


#live integration test (with real APIClient and DatabaseClient)
def test_register_user_integration():
    """Integration test for UserServices with real APIClient and DatabaseClient"""
    api_client= APIClient()
    db_client= DatabaseClient('test_users.db')
    servers= UserServices(api_client, db_client)

    result= servers.register_user('sulaimon majeed', 'sulaimonmajeed@example.com', 25)
    assert result == 'SULAIMON MAJEED'
