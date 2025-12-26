from flask import Flask, render_template, request
from datetime import datetime

server = Flask(__name__)

@server.route("/", methods=['GET'])
def homepage():
    return render_template("homepage.html")


@server.route('/welcome', methods=['GET'])
def welcome():
    return render_template("welcome.html", message="IoT Application")


@server.route('/temperatures', methods=['GET'])
def retrieve_temperatures():
    temps = [
        (27, 60, "hall", "2025-12-25 09:30"),
        (26, 55, "CT01", "2025-12-25 09:31"),
        (26, 58, "CT02", "2025-12-25 09:32"),
        (27, 62, "Library", "2025-12-25 09:33")
    ]
    return render_template("table.html", message=temps)


@server.route('/temperature', methods=['GET', 'POST'])
def add_temperature():
    if request.method == 'POST':
        temp = request.form.get('temp')
        humidity = request.form.get('humidity')
        loc = request.form.get('loc')
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"Temp = {temp}, Humidity = {humidity}, Location = {loc}, Time = {current_time}")

    return render_template("form.html")


if __name__ == '__main__':
    server.run(debug=True)
