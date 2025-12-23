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
    client.subscribe("home/+/control")

def on_message(client, userdata, msg):
    appliance = msg.topic.split("/")[1]
    status = msg.payload.decode()

    print(f"{appliance.upper()} turned {status}")

    sql = """
    INSERT INTO appliance_status (appliance_name, status)
    VALUES (%s, %s)
    """
    cursor.execute(sql, (appliance, status))
    db.commit()

    # Publish updated status
    client.publish(f"home/{appliance}/status", status)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()
