from typing import Dict

from fastapi import FastAPI, HTTPException, Response, status

from app.models import Employee, EmployeeCreate

app = FastAPI(
    title="Employee Management API",
    description="A beginner-friendly REST API for managing employees.",
    version="1.0.0",
)

employees: Dict[int, Employee] = {
    1: Employee(
        id=1,
        name="Alice Johnson",
        email="alice@example.com",
        department="Engineering",
        salary=75000.0,
    ),
    2: Employee(
        id=2,
        name="Bob Smith",
        email="bob@example.com",
        department="Human Resources",
        salary=62000.0,
    ),
}


@app.get("/employees", response_model=list[Employee])
def get_employees() -> list[Employee]:
    """Get all employees."""
    return list(employees.values())


@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int) -> Employee:
    """Get one employee by ID."""
    employee = employees.get(employee_id)
    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {employee_id} was not found.",
        )
    return employee


@app.post("/employees", response_model=Employee, status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeCreate) -> Employee:
    """Create a new employee."""
    new_id = max(employees.keys(), default=0) + 1
    new_employee = Employee(id=new_id, **employee.model_dump())
    employees[new_id] = new_employee
    return new_employee


@app.put("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: EmployeeCreate) -> Employee:
    """Update employee details by ID."""
    if employee_id not in employees:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {employee_id} was not found.",
        )

    updated_employee = Employee(id=employee_id, **employee.model_dump())
    employees[employee_id] = updated_employee
    return updated_employee


@app.delete("/employees/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(employee_id: int) -> Response:
    """Delete an employee by ID."""
    if employee_id not in employees:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {employee_id} was not found.",
        )

    del employees[employee_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
