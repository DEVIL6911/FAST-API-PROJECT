from fastapi import FastAPI
from models import Product
app = FastAPI()
@app.get("/")
def greet():
    return "Hello, World!"

product= [
    Product(id=1, name="Laptop", price=999.99, description="A high-performance laptop", quantity=10, category="Electronics"),
    Product(id=2, name="Smartphone", price=499.99, description="A latest model smartphone", quantity=25, category="Electronics"),
    Product(id=3, name="Headphones", price=199.99, description="Noise-cancelling headphones", quantity=15, category="Accessories"), 
    Product(id=4, name="Coffee Maker", price=79.99, description="Automatic coffee maker", quantity=30, category="Home Appliances"),
    Product(id=5, name="Gaming Console", price=399.99, description="Next-gen gaming console", quantity=20, category="Entertainment")

]

@app.get("/products")
def get_all_products():
    return product


@app.get("/products/{product_id}")
