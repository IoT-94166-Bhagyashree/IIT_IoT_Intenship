from flask import Flask,request

from utils_q1.execute_query_q1 import executeQuery
from utils_q1.execute_select_query_q1 import executeSelectQuery
from datetime import datetime
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>THIS IS HOME PAGE</h1></body></html>"

@server.post('/reading')
def create_readings():
    id = request.form.get('id')
    temperature = request.form.get('temperature')
    humidity = request.form.get('humidity')
    timestamp = request.form.get('timestamp')
    now =datetime.now()
    query = f"insert into sensor_readings values({id},{temperature},{humidity},'{now}')"
    
    executeQuery(query=query)
    
    
    return "readings is added successfully"


@server.get('/reading')
def retrive_readings():

    query = "select * from sensor_readings;"

    # execute select query
    data = executeSelectQuery(query=query)
    for i in data:
        return i


@server.put('/reading')
def update_readings():
    # extract data form form
    id = request.form.get('id')
    temperature = request.form.get('temperature')

    # create a query
    query = f"update sensor_readings SET temperature = {temperature} where id = {id};"

    # execute the query
    executeQuery(query=query)

    return "temperature is updated successfully"

@server.delete('/reading')
def delete_readings():
    # extract data form form
    id = request.form.get('id')

    # create a query
    query = f"delete from sensor_readings where id = {id};"

    # execute the query
    executeQuery(query=query)

    return "reading is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)

