from pydantic import BaseModel,Field,EmailStr
from typing import List,Optional


class Item(BaseModel):
  ids : int
  name : str = Field(...,title="provide me name",description="the description of name")
  price : float = Field(0.0,title="Item Price",description="the description of price is",ge=0)

item1 = Item(ids=1,name="coffee mug")

print(item1.name)
print(item1.ids)
print(item1.price)


# string validations

class Post(BaseModel):
  title:str = Field(...,min_length=0,max_length=50)
  currency: str = Field(...,min_length=0,max_length=12)

try:
  post = Post(title='my first pydantic',currency="IND")
  print(post.title)
  print(post.currency)
except Exception as e:
  print(e)


# Numberic
class Num(BaseModel):
  college_id: int = Field(...,ge=1,le=10,title="provide me here integer number ")
  registr_id : float = Field(223.34,ge=200,le=500)

try:
  num_store = {"college_id":12,"registr_id":333.3}
  num = Num(**num_store)
  print(num.college_id)
  print(num.registr_id)
except Exception as e:
  # print(e)
  print(f"Validation Error: {e}")

# 
# 4. Aliases and Regular Expressions (Regex)
class UserProfile(BaseModel):
  email: EmailStr = Field(...,alias="user_email",description="provide me email")
  name: str = Field("rohan",alias="user_name",description="provide me name",pattern=r"^[A-Za-z][A-Za-z0-9_]{3,15}$")
  age : Optional[int] = Field(None, description="give me the age")


try:
  store1 = {"user_email":"kishlaykumar@gmail.com","user_name":"kishlay","age":22}
  store2 = {"user_email":"rohankumar@gmail.com","age":25}
  reslt1 = UserProfile(**store1)
  reslt2 = UserProfile(**store2)

  print(reslt1.email)
  print("\n")
  print(reslt1)
  print("\n")
  print(reslt2)

except Exception as e:
  print(e)