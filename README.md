# Expense Tracker with Budget Alerts

## Overview
This is a full-stack **Expense Tracker** application built with **React (frontend)** and **FastAPI (backend)**. The app allows users to:
- **Track expenses** by adding and deleting items.
- **Set a budget** and receive alerts when nearing the limit.
- **Persist data** via API endpoints.

## Features
✅ Add, view, and delete expenses.  
✅ Set and update budget dynamically.  
✅ Alert when expenses reach **90% of the budget**.  
✅ Responsive UI built with **shadcn/ui**, **TailwindCSS**, and **Framer Motion**.  
✅ Fast and lightweight backend using **FastAPI**.  

---

## Tech Stack
- **Frontend:** React, TailwindCSS, shadcn/ui, Framer Motion
- **Backend:** FastAPI, Pydantic
- **Tools:** Fetch API for HTTP requests

---

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Node.js & npm
- Python 3.9+

### Clone Repository
```sh
git clone https://github.com/YOUR_USERNAME/expense-tracker.git
cd expense-tracker
```

### Backend Setup (FastAPI)
1. Install dependencies:
   ```sh
   pip install fastapi uvicorn
   ```
2. Run the server:
   ```sh
   uvicorn server:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`

### Frontend Setup (React)
1. Install dependencies:
   ```sh
   npm install
   ```
2. Run the development server:
   ```sh
   npm run dev
   ```
   The app will be available at `http://localhost:3000`

---

## API Endpoints
### Expenses
- **GET /expenses** → Retrieve all expenses.
- **POST /expenses** → Add a new expense.
- **DELETE /expenses/{index}** → Delete an expense.

### Budget
- **GET /budget** → Retrieve the current budget.
- **PUT /budget** → Update the budget.

---

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit and push your changes.
4. Open a pull request.

---

## License
This project is open-source and available under the **MIT License**.

---

## Contact
For issues or suggestions, create an [issue](https://github.com/Akajiaku1//expense-tracker/issues) .

---

🚀 **Happy Expense Tracking!**

