from quixstreams import Application
from pathlib import Path
import json
from pprint import pprint
data_path = Path(__file__).parents[1] / "data"

with open(data_path / "jokes.json", "r") as file:
    jokes = json.load(file)

# pprint(jokes)

app = Application(broker_address="localhost:9092", consumer_group="text-splitter")

jokes_topic = app.topic(name ="Jokes", value_serializer="json")

# print(jokes_topic)

def main():
    with app.get_producer() as producer:
        # print(producer)
        for joke in jokes:
            kafka_msg = jokes_topic.serialize(key=joke["joke_id"], value=joke)

            print(f"Produced message: key = {kafka_msg.key} value = {kafka_msg.value}")

            producer.produce(topic="jokes", key= str(kafka_msg.key), value= kafka_msg.value)

if __name__ == "__main__":
    main()
