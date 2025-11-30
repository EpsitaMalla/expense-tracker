from pydantic import BaseModel

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        from_attributes = True

class IncomeBase(BaseModel):
    amount: float
    description: str

class IncomeCreate(IncomeBase):
    user_id: int

class Income(IncomeBase):
    id: int
    user_id: int
    class Config:
        from_attributes = True

class ExpenseBase(BaseModel):
    amount: float
    description: str

class ExpenseCreate(ExpenseBase):
    user_id: int

class Expense(ExpenseBase):
    id: int
    user_id: int
    class Config:
        from_attributes = True
