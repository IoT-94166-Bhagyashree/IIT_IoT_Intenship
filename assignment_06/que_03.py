from flask import Flask, request

app = Flask(__name__)

#Store Temperature
@app.route('/send_temperature')
def send_temperature():
    temp = request.args.get('value')

    with open("temperature.txt", "a") as f:
        f.write(temp + "\n")

    return "Temperature stored successfully"


#store Light Intensity 
@app.route('/send_light')
def send_light():
    light = request.args.get('value')

    with open("light.txt", "a") as f:
        f.write(light + "\n")

    return "Light intensity stored successfully"


#Display Temperature 
@app.route('/get_temperature')
def get_temperature():
    with open("temperature.txt", "r") as f:
        data = f.read()
    return "<pre>" + data + "</pre>"


#Display Light 
@app.route('/get_light')
def get_light():
    with open("light.txt", "r") as f:
        data = f.read()
    return "<pre>" + data + "</pre>"


if __name__ == "__main__":
    app.run(debug=True)
