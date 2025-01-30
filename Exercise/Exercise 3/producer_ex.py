from quixstreams import Application
from pathlib import Path
import json

data_path = Path(__file__).parent /"Data/orders.json"

with open(data_path) as file:
    data = json.load(file)

app = Application(broker_address="localhost:9092", consumer_group="order-writer")

orders_topic = app.topic(name ="Orders", value_serializer="json")

def main():
    with app.get_producer() as producer:
        # print(producer)
        for order in data:
            kafka_msg = orders_topic.serialize(key=order["order_id"], value=order)

            print(f"Produced message: key = {kafka_msg.key} value = {kafka_msg.value}")

            producer.produce(topic="Orders", key= str(kafka_msg.key), value= kafka_msg.value)

if __name__ == "__main__":
    main()