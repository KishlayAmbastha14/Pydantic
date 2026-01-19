from pydantic import BaseModel,ValidationError,model_validator

from typing import List,Optional

class DATARange(BaseModel):
  start_date : str
  end_date : Optional[str]  = None

  @model_validator(mode="after")
  def check_dates_cohesion(self):
    start = self.start_date
    end = self.end_date

    if end and (end < start):
      raise ValueError("end date cannot be before the starat date")
    return self
  
range1 = DATARange(start_date="2024-01-10",end_date="2024-01-20")

print(f"Valid Range: {range1.start_date} to {range1.end_date}")