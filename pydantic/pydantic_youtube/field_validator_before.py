## 
##  2. field_validator Using mode='before'

from pydantic import BaseModel,field_validator,ValidationError
import re

class PhoneNumber(BaseModel):
  phone_number: str

  @field_validator("phone_number",mode="before")
  @classmethod
  def clean_phone_number(cls,v:str):
    if not isinstance(v,str):
      raise ValueError("Phone number must be str")
    
    cleaned_v = re.sub(r"\D","",v)

    if len(cleaned_v) < 10:
      raise ValueError("phone number must be 10 length")
    return cleaned_v
  
try: 
  phone_data = {"phone_number":"(555) 123-4567"}
  phone1 = PhoneNumber(**phone_data)
  print(f"Cleaned Phone : {phone1.phone_number}")

  phone2 = PhoneNumber(phone_number=1234567890)

  print(f"clenaed phone : {phone2.phone_number}")
except ValidationError as e:
  print(e)
