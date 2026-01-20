from pydantic import BaseModel,model_validator,ValidationError
from typing import List,Optional,Any



class Person(BaseModel):
  name:str
  age:int

  @model_validator(mode="before")
  def from_list(data:Any):
    data['name'] = data['name'].strip().title()

    if data['age'] < 0:
      raise ValueError('AGE should be greater than zero')
    return data

p1 = Person(name="yashh",age=34)
print(p1)
try: 
  p2 = Person(name="ksiha   laya ", age=-20)
  print(p2)
except ValidationError as e:
  print(e)