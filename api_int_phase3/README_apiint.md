
# 🚀 Phase 4 — API-to-Database Integration Framework

## Overview
In this phase, the BridgeX framework was tested with API sourced data.
The goal was to ensure that data from a diffrent API sourceS could be seamlessly integrated into the database layer through the PostgreConnect & DatabaseConnect modules — validating the system’s external data flow and connecting to real-world APIs.


## Implementation Details
- Classes Tested: `APIClient, PostgreConnect & DatabaseConnect, and RequestGet`
- Testing Framework: pytest
- Database Used: **SQLite3 & PostgreSQL** (Cloud DB e.g Neon console)
- Data Source: API sourced (simulated API-sourrced)
- Testing Objective: Validate successful data extraction, transformation, and persistence in the API test database.

## ⚙️ Architecture

The framework is divided into the following core components:

### 🧩 1. APIClient
- Fetches data from external APIs.
- Handles authentication, headers, and parameters dynamically.
- Returns normalized JSON data (via `pandas.json_normalize`).

### 🧱 2. PostgreConnect & DatabaseConnect
- Manages database operations (create, insert, fetch).
- Supports both **SQLite3** and **PostgreSQL** using **SQLAlchemy**.
- Can easily switch between local and cloud DBs.

### 🔗 3. RequestGet
- Connects APIClient and DatabaseConnect.
- Automates the flow of fetching → cleaning → saving → verifying data.
- Implements validation and error-handling logic.

---

## 🧾 Example PostgreSQL Setup

```python
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://username:password@localhost:5432/bridgex_db"
)
```

Switch between **SQLite3** and **PostgreSQL** effortlessly in your`PostgreConnect` & `DatabaseConnect` class.

---

## BridgeX-API-Integration/
├── bridgex_api_sqlite.py         # Phase 1 – API to SQLite integration
├── bridgex_api_postgresql.py     # Phase 2 – API to PostgreSQL integration
├── requirements.txt
└── README.md
---

# BridgeX API Integration (v2)

### 🌉 Overview
**BridgeX API Integration** is a Python-based data pipeline designed to fetch JSON data from an API endpoint, normalize it into a structured format using **Pandas**, and store it seamlessly into both **SQLite** and **PostgreSQL** databases.

This project is part of the **BridgeX Data Integration Series**, demonstrating real-world API ingestion, data transformation, and persistence workflows for Business Analysts and Data Engineers.

---

## ⚙️ Features

- Fetches live data from any API endpoint
- Converts complex JSON into tabular format using `pandas.json_normalize()`
- Supports **SQLite** (local testing) and **PostgreSQL** (cloud-ready)
- User-friendly — prompts you to enter your connection details interactively
- Easily extendable for other databases or APIs

---

## 🧩 Version Information

| Version | Description | Database Type |
|----------|--------------|----------------|
| **v1** | Initial version using SQLite for local integration | SQLite |
| **v2** | Extended version using SQLAlchemy for PostgreSQL integration | PostgreSQL |

---

## 🏗️ How It Works

1. Prompts the user for:
   - API URL  
   - Database connection details (username, password, host, port, database name)
2. Fetches API data and normalizes it into a Pandas DataFrame.
3. Writes the structured data into a specified database table.
---
