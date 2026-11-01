# Employee Management API

This project is a beginner-friendly REST API built with Python and FastAPI for managing employees.

## Features

- Get all employees
- Get an employee by ID
- Add a new employee
- Update employee details
- Delete an employee
- In-memory data storage
- Basic validation with HTTP status codes

## Project structure

- `app/main.py` - API routes and startup logic
- `app/models.py` - Employee data models and validation

## Installation

1. Open a terminal in the project folder.
2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the environment:

   On Windows:

   ```bash
   .venv\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

- http://127.0.0.1:8000
- Swagger docs: http://127.0.0.1:8000/docs

## API endpoints

- `GET /employees` - Get all employees
- `GET /employees/{id}` - Get employee by ID
- `POST /employees` - Add a new employee
- `PUT /employees/{id}` - Update employee details
- `DELETE /employees/{id}` - Delete an employee

## Example employee JSON

```json
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "department": "Finance",
  "salary": 80000
}
```
