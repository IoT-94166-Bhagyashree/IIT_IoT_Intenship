from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime
import paho.mqtt.client as mqtt

app = Flask(__name__)


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "smart_agriculture"
}

MQTT_BROKER = "test.mosquitto.org"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/moisture/alert"

MOISTURE_THRESHOLD = 30

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


@app.route("/moisture", methods=["POST"])
def store_moisture():
    data = request.json

    sensor_id = data.get("sensor_id")
    moisture_level = data.get("moisture_level")
    current_time = datetime.now()

    if sensor_id is None or moisture_level is None:
        return jsonify({"error": "Invalid input"}), 400

    # Insert into database
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO moisture_readings (sensor_id, moisture_level, datetime)
        VALUES (%s, %s, %s)
    """
    cursor.execute(query, (sensor_id, moisture_level, current_time))
    conn.commit()

    cursor.close()
    conn.close()

    
    if moisture_level < MOISTURE_THRESHOLD:
        alert_msg = f"ALERT! Sensor {sensor_id}: Moisture low ({moisture_level})"
        mqtt_client.publish(MQTT_TOPIC, alert_msg)

    return jsonify({"message": "Moisture data stored successfully"}), 200


@app.route("/moisture", methods=["GET"])
def get_moisture():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM moisture_readings")
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(records)


if __name__ == "__main__":
    app.run(debug=True)
