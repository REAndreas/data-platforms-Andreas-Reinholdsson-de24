from quixstreams import Application

app = Application(broker_address="localhost:9092", consumer_group="order-writer", auto_offset_reset="earliest")

orders_topic = app.topic(name= "Orders", value_deserializer="json")

sdf = app.dataframe(topic=orders_topic)

def order_output(order_data):
    total_price = 0
    print(f"Input: {order_data}")
    for product in order_data["products"]:
        print(f"Product: {product["name"]} quantity: {product["quantity"]} Price: {product["price"]}")
        total_price = product["quantity"] * product["price"] + total_price
    print(f"Total price: {total_price:.2f}")

sdf = sdf.update(order_output)

if __name__ == "__main__":
    app.run()