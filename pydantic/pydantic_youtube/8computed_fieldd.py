from pydantic import BaseModel,computed_field,Field

from typing import List,Optional

## IMPORTANT OF COMPUTED_FIELD AND Property 


class Employee(BaseModel):
  first_name: str
  last_name : str


  @computed_field
  @property
  def full_name(self) -> str:
    return f"{self.first_name} {self.last_name}"


res = Employee(first_name='kishlay',last_name='kumar')
# print(res.full_name) 
# print(f"Employee Name: {res.full_name}")


### ------------ second questions

class IncomeTax(BaseModel):
  name: str = Field(...,description='give me your name')
  item_id: int = Field(...,description="provide me your id ",ge=1,le=100)
  unit_price : float
  quantity: int
  tax_rate : float = 0.05


  @computed_field
  @property
  def total_price(self) -> float:
    return round(self.unit_price * self.quantity, 2)
  
  @computed_field
  @property
  def total_tax_rate(self) -> float:
    taxes = self.total_price * self.tax_rate
    return round(self.total_price + taxes,2)


results = {"name":"Kishlay","item_id":34,"unit_price":11,"quantity":4}
order1 = IncomeTax(**results)

# print(order1)


# ### questions 
# 🟢 QUESTION 1 (Easy – Warm-up)
# 📌 Scenario
# Tum ek Student model bana rahe ho.
# Fields:
# first_name: str
# last_name: str
# marks: int (out of 100)
# Task:
# 1️⃣ Create a computed field full_name
# 2️⃣ Create a computed field result
# "Pass" if marks ≥ 40
# "Fail" otherwise
# Rules:
# Use @computed_field
# Use @property
# result must appear in output
# 🧠 Hint:
# @property alone is not enough

class Student(BaseModel):
  first_name: str = Field(...,description="provide me your first name")
  last_name : str = Field(..., description = "provide me your second name")
  marks : int = Field(...,ge=1, le=100)

  @computed_field
  @property
  def full_name(self) -> str:
    return f"{self.first_name}{self.last_name}"
  
  @computed_field
  @property
  def result(self) -> str:
    if(self.marks >= 40):
      return f"this students is PASSED"
    else:
      return f"this students is FAILED"
    
s1 = Student(first_name="Kishlay",last_name="Kumar",marks=56)

# print(s1)
# print(s1.full_name)
# print(s1.result)
    
# 🟡 QUESTION 2 (Medium – Calculation Based)
# 📌 Scenario
# You are building a Shopping Cart Item.
# Fields:
# product_name: str
# price: float
# quantity: int
# discount_percent: float = 10
# Task:
# Create computed fields:
# 1️⃣ discount_amount
# 2️⃣ price_after_discount
# 3️⃣ total_price
class ShoppingCart(BaseModel):
  product_name : str
  price : float
  quantity : int
  discount_percent : float = 10

  @computed_field
  @property
  def discount_amount(self) -> int:
    return (self.price * (self.discount_percent/100))
  
  @computed_field
  @property
  def price_after_discount(self) -> int:
    return self.price - self.discount_amount
  
  # iha ydi humlog computed use nhi krenge to isse ye ek trh se noraml smjhega and isse pydnatic me use nhi krega which is not good for us thats why we use computed field 
  @computed_field
  @property
  def total_price(self) -> int:
    return self.price_after_discount * self.quantity

  # Formula:
# discount_amount = price * (discount_percent / 100)
# price_after_discount = price - discount_amount
# total_price = price_after_discount * quantity

# Conditions:

# Round values to 2 decimals

# total_price should use other computed fields


s1 = ShoppingCart(product_name="MANGO",price=300.20,quantity=4)
print(s1)
print(s1.discount_amount)
print(s1.price_after_discount)
print(s1.total_price)







# 🟡 QUESTION 3 (Understanding Difference)
# 📌 Scenario
# Create a User model:
# Fields:
# age: int
# Tasks:
# 1️⃣ Create a property is_adult
# 2️⃣ Create a computed_field age_group
# "Child" (< 18)
# "Adult" (18–60)
# "Senior" (> 60)
# Question (VERY IMPORTANT):
# 👉 Which one will appear in .model_dump() and WHY?

# (Answer in words, not code)

# 🔵 QUESTION 4 (Advanced – Dependency & Logic)
# 📌 Scenario

# You are building an Employee Payroll system.

# Fields:

# basic_salary: float

# hra: float

# bonus: float = 0

# tax_rate: float = 0.1

# Task:

# Create computed fields:
# 1️⃣ gross_salary

# gross = basic + hra + bonus


# 2️⃣ tax_amount
# 3️⃣ net_salary

# Conditions:

# tax_amount depends on gross_salary

# net_salary = gross_salary - tax_amount

# 🧠 Hint:

# Computed fields can depend on other computed fields

# 🔴 QUESTION 5 (Thinking / Interview Level 🔥)
# 📌 Scenario

# You created a computed field total_price.

# Now answer conceptually:

# 1️⃣ Can user pass total_price in input data? Why?
# 2️⃣ Is computed_field stored in database?
# 3️⃣ When should you use computed_field instead of calculating in frontend?

# (No code, just explanation)

# 🧠 MEMORY CHECK (VERY IMPORTANT)

# Fill in the blanks:

# 1️⃣ @property → used for __________ logic
# 2️⃣ @computed_field → appears in __________
# 3️⃣ Computed fields are calculated at __________ time
# 4️⃣ Computed fields are based on __________ fields

# 🎯 BONUS MINI TASK (REAL PORTFOLIO IDEA)

# Write a small blog section titled:

# “computed_field vs property in Pydantic (with examples)”

# Include:

# one code example

# one table

# one mistake beginners make

# (Just outline, not full blog)