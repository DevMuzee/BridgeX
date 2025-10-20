import sqlite3
import requests

class APIClient:
    """Simulate an external API Client"""
    def get_user_data(self, username, email, age):
        response= requests.get(f"http://api.example.com/users?username={username}&email={email}&age={age}")
        if response.status_code == 200:
            return response.json()
        raise ValueError("API request failed")


class DatabaseClient:
    def __init__(self, db_name= 'users.db'):
        self.db_name= db_name
        self._create_table()
    
    def _create_table(self):
        """CREATING the table to store the data fetched from API"""
        conn= sqlite3.connect(self.db_name)
        cursor= conn.cursor()
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT,
            age INT CHECK(age >= 0)
            )
            '''
        )
        conn.commit()
        conn.close()

    
    def save_user(self, username, email, age):
        conn= sqlite3.connect(self.db_name)
        cursor= conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, age) VALUES (?, ?, ?)", (username, email, age)
        )
        conn.commit()

        #fetching the inserted data
        cursor.execute(
            "SELECT username, email, age FROM users WHERE email= ?", (username, email, age)
        )
        user_get= cursor.fetchone()
        conn.close()

        if user_get:
            return {
                'username':user_get[0],
                'email': user_get[1],
                'age': user_get[2]
            }


class UserServices:
    def __init__(self, api_client, db_client):
        self.api_client= api_client
        self.db_client= db_client

    def register_user(self, username, email, age):
        """Testing for age lesser than 0 inputed"""
        if age <= 0:
            raise ValueError("Age cannot be negative")
        
        """Fetch from the API, save to DB and return the username as a uppercase"""
        api_get= self.api_client.get_user_data(username, email, age)
        user_get= self.db_client.save_user(api_get['username'], api_get['email'], api_get['age'])
        return user_get['username'].upper()

#result format
# api= APIClient()
# db= DatabaseClient()
# service= UserServices(api, db)
# result= service.register_user('username', 'email', 'age')