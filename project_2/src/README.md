# DecodeLabs: Expense Tracker Backend Engine (Phase 2)

A robust, CLI-based financial tracking application built with Python. This project demonstrates core backend programming concepts including state persistence, continuous data streaming loops, defensive input validation (Poka-Yoke), and structured error-handling mechanisms to prevent system crashes.

---

## 🚀 Key Features

* **Continuous Data Stream:** Utilizes an active engine loop (`while True`) to capture real-time financial logs from the user without restarting the application.
* **State Accumulation (Memory Stage):** Eliminates data amnesia by maintaining tracking variables outside the main processing loop to keep a persistent running total across the entire session.
* **Digital Poka-Yoke (Error-Handling Barrier):** Features advanced exception handling (`try-except`) to intercept non-numeric entry attempts (e.g., text, special characters) and gracefully prevent process termination or unexpected crashes.
* **Defensive Validation Checks:** Automatically blocks logical financial anomalies, such as negative expenditure inputs, ensuring data integrity.
* **Sentinel / Kill Switch:** Smooth terminal exit mechanics via `exit` or `quit` commands that gracefully break the execution stream and route to the final financial audit.

---

## 🛠️ Tech Stack & Concepts

* **Language:** Python 3.x
* **Architecture:** Procedural CLI Engine
* **Key Paradigms:** 
  * State Management & Persistence
  * Defensive Programming (Poka-Yoke)
  * Exception Routing (`ValueError`)
  * Data Transformation (`string` to `float`)

---

## 📂 Project Structure

```bash
├── expense_tracker.py   # Core Python logic and backend engine
└── README.md            # Documentation and execution guide

python expense_tracker.py
