
# BridgeX Unified API Integration (Phase 5)

This project is the **Phase 5** release of the BridgeX API Integration System — a unified and interactive solution that connects APIs with databases, enabling users to extract, process, and store API data in either **SQLite**, **PostgreSQL**, or **both**, based on their selection.

---
`
## 🚀 Features
- Interactive **CLI-based user interface**
- Fetches data from any user-provided API URL
- Supports saving data to:
  - **SQLite Database**
  - **PostgreSQL Database**
  - **Both SQLite and PostgreSQL**
- Ensures smooth operation through user input validation and feedback loops
- Provides detailed success/failure messages for transparency

---

## 🧩 How It Works

1. **User Input Phase**
   - The program prompts for the API URL.
   - It fetches the API data and normalizes it into a Pandas DataFrame.

2. **Database Selection Phase**
   - Users can choose where to store their data:
     - `1` → Save to SQLite
     - `2` → Save to PostgreSQL
     - `3` → Save to both SQLite and PostgreSQL
     - `exit` → Quit the program

3. **Database Connection Phase**
   - For SQLite: Automatically handles database file creation.
   - For PostgreSQL: Prompts user to enter database credentials (user, password, host, port, and db name).

4. **Data Storage Phase**
   - Data is saved into the chosen database(s) with feedback confirmation.

---

## 🛠️ Requirements

- Python 3.8 or higher
- Install dependencies using:
  ```bash
  pip install pandas sqlalchemy psycopg2 requests
  ```

---

## ▶️ How to Run

1. Clone this repository or download the code files.
2. Run the Python script:
   ```bash
   python bridgeX_unified_api_integration.py
   ```
3. Follow the on-screen instructions to provide API URL and select preferred database storage.

---

## ⚙️ Example Usage

```
--- BridgeX Unified API Integration ---
Enter your API URL: https://api.example.com/data

✅ API Data fetched successfully with 120 records.

Where would you like to save your data?
1️⃣  SQLite Database
2️⃣  PostgreSQL Database
3️⃣  Both
🔚  Type 'exit' to quit

Enter your choice (1/2/3 or 'exit'): 3

✅ Data successfully saved to both SQLite and PostgreSQL databases.
```

---

## 📦 Output

- **SQLite:** Saved locally as `bridgeX_data.db`
- **PostgreSQL:** Data inserted into the specified table within the provided database

---

## 🧠 Author’s Note

This version represents a major milestone in the BridgeX journey — evolving from simple data fetching to a fully interactive, database-agnostic integration system.  
The next phase (v6) will introduce **a Streamlit web-based interface**, turning this CLI experience into a visual dashboard.

---

**Author:** Adewale Abdulmuiz Akorede  
**Project:** BridgeX API Integration System — Phase 5  
**Challenge:** #100DaysOfCoffeeAndCode ☕  
**LinkedIn:** [Adewale Abdulmuiz (Akorede)](https://www.linkedin.com/in/abdulmuiz-akorede)

