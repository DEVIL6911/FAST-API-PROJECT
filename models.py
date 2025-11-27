
from pydantic import BaseModel

class Product(BaseModel):  # ya line dal na sa constructor bana na ke zarurat nahi hoti 
    id : int
    name : str
    price : float
    description : str
    quantity: int
    category: str

     