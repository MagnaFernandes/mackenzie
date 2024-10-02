import json
import time
from kafka import KafkaProducer
from faker import Faker

fake = Faker()
bootstrap_servers = ['kafka:9092']
topicName = 'faker-data'

producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    data = {
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email()
    }
    producer.send(topicName, value=data)
    print(f"Sent data: {data}")
    time.sleep(1) # Adjust sending frequency as needed