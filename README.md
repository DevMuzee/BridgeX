# 🧩 BridgeX — API-to-Database Integration Framework (Beta Stage)

**BridgeX** is a lightweight, modular Python framework that simulates and manages seamless data integration between external APIs and local databases.  
It is designed to demonstrate core concepts of modern data engineering pipelines — **fetching**, **transforming**, and **storing** structured data — while maintaining a clean service-oriented architecture.

---

## 🚀 Project Status
**Current Stage:** `Beta (Integration Testing Phase)`  
**Completed Milestones:**  
✅ Mock API Simulation (Alpha Stage)  
✅ Unit Testing (All Core Classes Passed)  
🟡 Integration Testing (In Progress)  

---

## 🏗️ Architecture Overview
BridgeX follows a **three-layer architecture**, designed for clarity, scalability, and easy testing.

```
APIClient  →  UserServices  →  DatabaseClient
   ↓             ↓                 ↓
 Fetch       Process/Logic       Store
```

- **APIClient** — Handles all external API interactions, fetching user data via HTTP requests.  
- **DatabaseClient** — Manages persistent storage of data using SQLite (or extendable DB engines).  
- **UserServices** — The logic layer that connects API and Database clients, transforms data, and returns processed results.

---

## 📦 Features

- 🔗 **Seamless API–Database Bridge** — Fetches real-time data and persists it locally.  
- ⚙️ **Clean Service-Layer Design** — Decoupled architecture for scalability.  
- 🧪 **Comprehensive Unit Tests** — Mock-based testing for reliability.  
- 💾 **SQLite-Powered Storage** — Simple, lightweight, and portable database integration.  
- 🧱 **Extensible Architecture** — Plug-and-play capability for future REST, GraphQL, or NoSQL APIs.  
- 🔍 **Ready for Integration Tests** — Supports connection with real or mock APIs for end-to-end validation.

---

## 📁 Project Structure

```
BridgeX/
├── rev.py                 # Core source code (APIClient, DatabaseClient, UserServices)
├── test_rev.py            # Unit tests using pytest and mocker
├── requirements.txt       # Project dependencies
├── README.md              # Documentation (this file)
└── test_users.db          # Test database (auto-generated during runs)
```

---

## 🧠 Core Components

### 🧩 APIClient
Responsible for making GET requests to fetch user data from an external API.

```python
response = requests.get(
    f"http://api.example.com/users?username={username}&email={email}&age={age}"
)
```

*Future Upgrade:* Replace `api.example.com` with a real or locally simulated Flask/FastAPI endpoint for integration testing.

---

### 💾 DatabaseClient
Handles all database interactions such as saving user data or retrieving existing records.

```python
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (username, email, age))
```

*Supports*: SQLite (default), extendable for PostgreSQL or MySQL.

---

### ⚙️ UserServices
Connects API and DB layers — fetches data, saves to DB, and returns processed output.

```python
def register_user(self, username, email, age):
    api_get = self.api_client.get_user_data(username, email, age)
    user_get = self.db_client.save_user(api_get['username'], api_get['email'], api_get['age'])
    return user_get['username'].upper()
```

---

## 🧪 Testing

### ✅ Unit Tests
Located in `test_rev.py`, using **pytest** and **pytest-mock**.

```bash
pytest -v
```

These tests:
- Mock both API and database interactions.
- Validate method calls and output integrity.
- Ensure the service logic behaves correctly without real API calls.

### ⚙️ Integration Tests (Beta)
This stage involves replacing the mock API with:
- A **real** public API (e.g., `https://randomuser.me/api`), or  
- A **local Flask/FastAPI** simulation endpoint.

Example Integration Test:
```python
def test_register_user_integration():
    api_client = APIClient()
    db_client = DatabaseClient('test_users.db')
    services = UserServices(api_client, db_client)

    result = services.register_user('sulaimon majeed', 'sulaimonmajeed@example.com', 25)
    assert result == 'SULAIMON MAJEED'
```

---

## ⚡ Setup & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/BridgeX.git
cd BridgeX
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run unit tests
```bash
pytest -v
```

### 4️⃣ Run integration test (after API setup)
```bash
pytest -v -k "integration"
```

---

## 🧰 Requirements

| Package | Purpose |
|----------|----------|
| `requests` | API communication |
| `pytest` | Unit testing |
| `pytest-mock` | Mocking dependencies |
| `sqlite3` | Local data storage (built-in) |

*(Include these in your `requirements.txt`)*

---

## 🧩 Future Roadmap

| Stage | Description |
|--------|-------------|
| **v1.0.0** | Full integration testing with real API |
| **v1.1.0** | Add duplicate record handling and input validation |
| **v1.2.0** | Implement async requests using `aiohttp` |
| **v1.3.0** | Introduce configuration files and environment variables |
| **v2.0.0** | Deploy BridgeX as a microservice (FastAPI + PostgreSQL) |

---

## 🧑‍💻 Developer Notes

- BridgeX was designed as a **learning and portfolio project** showcasing practical Python architecture for data integration.  
- The framework can evolve into a **production-ready middleware layer** with more robust error handling and configuration management.  
- Ideal for demonstrating knowledge in **data engineering, API integration, and software testing**.

---

## 🏁 Author

- ** Developed by:** Adewale Abdulmuiz Akorede
- M[adewaleabdulmuiz75@gmail.com](mailto:adewaleabdulmuiz75@gmail.com)  )
- ~[LinkedIn – Abdulmuiz (Akorede) Adewale](https://www.linkedin.com/in/abdulmuiz-akorede)

---

## 🏷️ License
This project is released under the **MIT License** — free for learning, modification, and contribution.

---

## 🏁 Current Project Status
✅ Mock/Unit Test Stage — *Completed*  
✅ Local Integration Test — *Completed*  
🔄 API Integration Test — *In Progress*  
🚀 Final Deployment — *Upcoming*  

---

