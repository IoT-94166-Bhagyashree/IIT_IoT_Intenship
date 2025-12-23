import paho.mqtt.client as mqtt
import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_home"
)
cursor = db.cursor()

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe("sensor/ldr")
    client.subscribe("sensor/lm35")

def on_message(client, userdata, msg):
    topic = msg.topic
    value = float(msg.payload.decode())

    if topic == "sensor/ldr":
        sensor_type = "LDR"
    elif topic == "sensor/lm35":
        sensor_type = "LM35"

    sql = "INSERT INTO sensor_data (sensor_type, value) VALUES (%s, %s)"
    cursor.execute(sql, (sensor_type, value))
    db.commit()

    print(f"Stored {sensor_type} Value: {value}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
