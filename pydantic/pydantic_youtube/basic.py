from pydantic import BaseModel
from typing import List,Optional


class Post(BaseModel):
  idd:int
  age:int 
  title:str
  descrp: Optional[str] = None
  is_active:Optional[bool] = None


post= Post(idd=1,age=20,title="hello kishlay")
print(post.age)

try:
  post_dict = {"idd":123,"age":20,"title":"hello rohan"}
  post1 = Post(**post_dict)
  print(post1)
  print(post1.is_active)
except Exception as e:
  print(f"validations erros is : {e}")

