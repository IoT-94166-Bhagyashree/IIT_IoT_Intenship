import paho.mqtt.client as mqtt
import random
import time

broker = "localhost"
port = 1883

client = mqtt.Client()
client.connect(broker, port, 60)

while True:
    # Simulated sensor values
    ldr_value = random.randint(100, 900)
    temp_value = round(random.uniform(20, 35), 2)

    client.publish("sensor/ldr", ldr_value)
    client.publish("sensor/lm35", temp_value)

    print(f"Published LDR: {ldr_value}")
    print(f"Published Temperature: {temp_value}")

    time.sleep(5)
