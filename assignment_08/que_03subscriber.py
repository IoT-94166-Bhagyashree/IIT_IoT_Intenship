import paho.mqtt.client as mqtt
import mysql.connector

# Thresholds
PULSE_MIN = 60
PULSE_MAX = 100
SPO2_MIN = 95

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="healthcare"
)
cursor = db.cursor()

def send_alert(message):
    print("ALERT:", message)
    client.publish("patient/alert", message)

    cursor.execute(
        "INSERT INTO alerts (message) VALUES (%s)",
        (message,)
    )
    db.commit()

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker")
    client.subscribe("patient/pulse")
    client.subscribe("patient/spo2")

def on_message(client, userdata, msg):
    parameter = msg.topic.split("/")[1]
    value = float(msg.payload.decode())

    cursor.execute(
        "INSERT INTO patient_data (parameter, value) VALUES (%s, %s)",
        (parameter, value)
    )
    db.commit()

    print(f"{parameter.upper()} = {value}")

    # Alert conditions
    if parameter == "pulse":
        if value < PULSE_MIN or value > PULSE_MAX:
            send_alert(f"Pulse rate abnormal: {value} bpm")

    if parameter == "spo2":
        if value < SPO2_MIN:
            send_alert(f"Low SpO2 level: {value}%")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
