from pydantic import BaseModel,field_validator,ValidationError,Field

from typing import List,Dict,Optional,ClassVar


## --- FIELD VALIDATOR (AFTER) 


class UserPreference(BaseModel):
  theme_color:str
  font_size:int
  VALID_COLORS : ClassVar[list[str]] = ["dark","yellow","red"]

@field_validator("theme_color")
@classmethod
def check_valid_color(cls,v:str) -> str:
  v_lower = v.lower()
  if v_lower not in cls.VALID_COLORS:
    raise ValueError(f"Invalid color {v}Must be one of: {', '.join(cls.VALID_COLORS)}")
  return v_lower

user1 = UserPreference(theme_color="Dark",font_size=12)
print(f"User 1 Color (Transformed): {user1.theme_color}")

user2 = UserPreference(theme_color="PINK",font_size=14)
print(f"User 1 color {user2.theme_color},{user2.font_size}")

# ------------------------


class UserSettings(BaseModel):
  language:str=Field(...,description='add the languages')
  font_size:int=Field(ge=10,le=30,description="add the font size")
  VALID_LANGUAGES: ClassVar[list[str]] = ["en","hi","fr"]

  @field_validator("language")
  @classmethod
  def check_valid_lang(cls,v:str) -> str:
    v_lower = v.lower()

    if v_lower not in cls.VALID_LANGUAGES:
      raise ValueError(f"invalid colors {v} must be one of: {', '.join(cls.VALID_LANGUAGES)}")
    return v_lower
  

lang1 = UserSettings(language="EN",font_size=18)
print(lang1)


class InventoryItem(BaseModel):
  stock_level:int

  @field_validator("stock_level")
  @classmethod
  def check_stock_level(cls,v:int) -> int:
    if v<0:
      raise ValueError("Stock level not negative")
    return v
  
result = InventoryItem(stock_level="10")
print(result.stock_level)

try:
  result2 = InventoryItem(stock_level="-10")
  print(result2.stock_level)
except ValidationError as e:
  print(e)