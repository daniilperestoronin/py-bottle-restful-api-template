from bottle import request, route
import json

data = {"user2_proximity": 3, "Wifi_1": -80, "Wifi_2": -40, "Wifi_3": -40,
        "thermostat": 18, "light": 0, "hour_of_day": 0, "user3_proximity": 3,
        "user1_proximity": 1, "day_of_week": 1, "security": 0, "minute_of_hour": 9,
        "Act_1": 1, "Act_2": 0, "Act_3": 0}


@route('/notes/', method='POST')
def create():
    data = request.json
    return data


@route('/notes/<id_note>', method='GET')
def read(id_note):
    return json.dumps(data)


@route('/notes/', method='PUT')
def update():
    data = request.json
    return data


@route('/notes/<id_note>', method='DELETE')
def delete(id_note):
    return json.dumps(data)


@route('/notes/', method='GET')
def read_all():
    return json.dumps(data)
