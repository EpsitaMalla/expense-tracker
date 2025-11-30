# Expense Tracker API

A FastAPI-based REST API for tracking income and expenses with SQLAlchemy ORM.

## Features

- User management (create and retrieve users)
- Income tracking
- Expense tracking
- Financial reports (total income, expenses, and balance per user)
- SQLite database persistence
- Automatic schema creation on startup

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd expense-tracker
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   
   On Linux/macOS:
   ```bash
   source venv/bin/activate
   ```
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the development server with hot-reload enabled:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

### Access API Documentation

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## API Endpoints

### Health Check
- `GET /` - Check if the API is running

### Users
- `POST /users/` - Create a new user
  ```json
  {
    "name": "John Doe"
  }
  ```
- `GET /users/{user_id}` - Get user details by ID

### Income
- `POST /incomes/` - Add income
  ```json
  {
    "user_id": 1,
    "amount": 5000.00,
    "description": "Monthly salary"
  }
  ```

### Expenses
- `POST /expenses/` - Add expense
  ```json
  {
    "user_id": 1,
    "amount": 50.00,
    "description": "Groceries"
  }
  ```

### Reports
- `GET /report/{user_id}` - Get financial summary for a user
  ```json
  {
    "total_income": 5000.00,
    "total_expense": 150.00,
    "balance": 4850.00
  }
  ```

## Project Structure

```
expense-tracker/
├── app/
│   ├── main.py          # FastAPI application and routes
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic request/response schemas
│   └── database.py      # Database configuration
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── expense_tracker.db  # SQLite database (created at runtime)
```

## Technologies Used

- **FastAPI** - Modern web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **Pydantic** - Data validation using Python type hints
- **Uvicorn** - ASGI server
- **SQLite** - Lightweight database

## Development Notes

- The application uses SQLite for simplicity; for production, consider PostgreSQL or MySQL
- Database tables are automatically created on first run
- Hot-reload is enabled for development (`--reload` flag)
- All responses follow REST conventions with appropriate status codes

## Stopping the Server

Press `CTRL+C` in the terminal to stop the development server.

## Troubleshooting

**Port already in use:**
If port 8000 is already in use, specify a different port:
```bash
uvicorn app.main:app --reload --port 8001
```

**Database locked error:**
Delete `expense_tracker.db` and restart the application to reset the database.

## License

This project is open source and available under the MIT License.
