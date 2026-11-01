from pydantic import BaseModel, EmailStr, Field


class EmployeeBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    department: str = Field(..., min_length=1, max_length=100)
    salary: float = Field(..., gt=0)
    location: str = Field(..., min_length=1, max_length=100)


class Employee(EmployeeBase):
    id: int


class EmployeeCreate(EmployeeBase):
    pass
