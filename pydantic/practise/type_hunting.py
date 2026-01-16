from pydantic import BaseModel,Field
from typing import List,Dict

### ------- HERE WE USED BOTH THE LIST AND DICT


class Student(BaseModel):
  name:str = Field(...,max_length=100,description="provide me your name")
  age: int = Field(...,ge=1,le=100,json_schema_extra={"description": "provide me your age"})
  subject : List[str] = None

class Skills(BaseModel):
  skill_name: str = Field(...,max_length=100,description="provide me the skill name")
  tech_stack : Dict[str,str]
  total_skills : List[int]
  experience: int = Field(...,ge=1,le=5)

try: 
  s1 = Student(name='rohan',age=24,subject=['DSA,CN,DBMS,OOOPS'])
# print(s1)
  res = {"skill_name":'MACHINE LEARNING',
       "tech_stack":{"Python":"best","Models":"XGB"},
       "total_skills": [2,3],
       "experience" : 1}

  skills_part = Skills(**res)

  print(skills_part)
except Exception as e:
  print(e)
finally:
  print("no error was there")
