import paho.mqtt.client as mqtt

broker = "localhost"
port = 1883

client = mqtt.Client()
client.connect(broker, port, 60)

while True:
    print("\n1. Light ON")
    print("2. Light OFF")
    print("3. Fan ON")
    print("4. Fan OFF")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        client.publish("home/light/control", "ON")
    elif choice == '2':
        client.publish("home/light/control", "OFF")
    elif choice == '3':
        client.publish("home/fan/control", "ON")
    elif choice == '4':
        client.publish("home/fan/control", "OFF")
    elif choice == '5':
        break
    else:
        print("Invalid choice")

client.disconnect()
