from pathlib import Path
import json
from pprint import pprint

data_path = Path(__file__).parent / "Data"

with open(data_path / "orders.json") as file:
    order_data = json.load(file)

for order in order_data:
    total_price = 0
    print(f"Input: {order}")
    for product in order["products"]:
        print(f"Product: {product["name"]} quantity: {product["quantity"]} Price: {product["price"]}")
        total_price = product["quantity"] * product["price"] + total_price
    print(f"Total price: {total_price:.2f}")
        