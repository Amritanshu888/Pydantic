## Tab 1
# Pydantic Basics: Creating and Using Models
# Pydantic models are the foundation of data validation in Python. They use Python type annotations to define the structure and validate data at runtime. Here's a detailed exploration of basic model creation with several examples.

from pydantic import BaseModel

## Tab 2
from dataclasses import dataclass

@dataclass
class Person():
    name:str
    age:int
    city:str

person=Person(name="Krish",age=35,city="Bangalore")
print(person)

## Tab 3
person=Person(name="Krish",age=35,city=35)
print(person)

## Tab 4
class Person1(BaseModel):
    name:str
    age:int
    city:str

person=Person1(name="Krish",age=35,city="Bangalore")
print(person)

## Tab 5
person1=Person1(name="Krish",age=35,city=12)
print(person1)

## Tab 6
# 2. Model with Optional Fields
# Add optional fields using Python's Optional type:

from typing import Optional
class Employee(BaseModel):
    id: int
    name: str
    department: str
    salary: Optional[float] = None  # Optional with default value
    is_active: Optional[bool] = True  # Optional with default True

## Tab 7
# Examples with and without optional fields
emp1 = Employee(id=1, name="John", department="IT")
print(emp1)  # id=1 name='John' department='IT' salary=None is_active=True

## Tab 8
emp2 = Employee(id=2, name="Jane", department="HR", salary=60000, is_active=False)
print(emp2)

## Tab 9
# Definition:

# - Optional[type]: Indicates the field can be None

# - Default value (= None or = True): Makes the field optional

# - Required fields must still be provided

# - Pydantic validates types even for optional fields when values are provided

from pydantic import BaseModel
from typing import List

class Classroom(BaseModel):
    room_number: str
    students: List[str]  # List of strings
    capacity: int

## Tab 10
# Create a classroom
classroom = Classroom(
    room_number="A101",
    students=("Alice", "Bob", "Charlie"),
    capacity=30
)
print(classroom)

## Tab 11
try:
    invalid_val=Classroom(room_number="A1",students=["Krish",123],capacity=30)
except ValueError as e:
    print(e)

## Tab 12
# 4. Model with Nested Models
# Create complex structures with nested models:

from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    zip_code: int

class Customer(BaseModel):
    customer_id: int
    name: str
    address: Address  # Nested model

# Create a customer with nested address
customer = Customer(
    customer_id=1,
    name="Emma",
    address={"street": "123 Main St", "city": "Boston", "zip_code": "02108"}
)
print(customer)

## Tab 13
# Pydantic Fields: Customization and Constraints
# The Field function in Pydantic enhances model fields beyond basic type hints by allowing you to specify validation rules, default values, aliases, and more. Here's a comprehensive tutorial with examples.

from pydantic import BaseModel,Field
class Item(BaseModel):
    name:str=Field(min_length=2,max_length=50)
    price:float= Field(gt=0,le=1000) #greater than 0, less than or equal to 1000
    quantity:int=Field(ge=0)

# Valid instance
item = Item(name="Book", price=10, quantity=10)

print(item)

## Tab 14
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(..., description="Unique username for the user")
    age: int = Field(default=18, description="User age, defaults to 18")
    email: str = Field(default_factory=lambda: "user@example.com", description="Default email address")

# Examples
user1 = User(username="alice")
print(user1)  # username='alice' age=18 email='user@example.com'

user2 = User(username="bob", age=25, email="bob@domain.com")
print(user2)  # username='bob' age=25 email='bob@domain.com'

## Tab 15
print(User.model_json_schema())