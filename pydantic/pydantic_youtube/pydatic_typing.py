
from typing import List,Literal,Optional
from pydantic import BaseModel
from enum import Enum

class Product(BaseModel):
  product_id: str
  tags:List[str]
  in_stock: Optional[int] = None

try:
  valid_Product = {"product_id":"12","tags":["electroics","utensils"]}
  total_product = Product(**valid_Product)
  # print(total_product)
  print(f" this is the total product is this {total_product.product_id},\n this is the product {total_product.tags[0]}")

except ValueError as e:
  print(e)

# print(int("10") + int("20"))

# STATIC TYPE CHEKING
class Book(BaseModel):
  idd : str
  author : List[str]


def process_book(book:Book):
  print(book.idd)

try:
  stored_book = Book(idd="P-24",author=["rohan","ramesh"])
  process_book(stored_book)
except Exception as e:
  print(e)


# TYPE ALIAS AND STANDARD TYPES
class Status(Enum):
  PENDING = "pending"
  COMPLETE = "complete"
  FAILED = "failed"

Transcation_type = Literal["depoist","withdrawal","transfer"]

class Transaction(BaseModel):
  type : Transcation_type
  status : Status

transaction_1 = Transaction(type="depoist",status=Status.PENDING)
print(f"Valid type and status: {transaction_1.type}, {transaction_1.status.value}")

