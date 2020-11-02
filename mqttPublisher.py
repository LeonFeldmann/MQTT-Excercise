import paho.mqtt.client as mqtt
import datetime
import random
import json
import time
import paho.mqtt.publish as publish


TOPIC = "iotcourse/channel"
device_id = 2500
latitude = "30.26"
longitude = "-97.73"
temp = 20


def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
    pass


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect("test.mosquitto.org", 1883, 60)

mqttc.loop_start()

while True:
    now = datetime.datetime.now()
    temp = random.randint(0, 35)

    # dd/mm/YY H:M:S
    dt_string = datetime.datetime.utcnow().strftime(
        '%d.%m.%Y %H:%M:%S.%f')[:-3]
    message = {
        "time": dt_string,
        "id": device_id,
        "temp": temp,
        "latitude": latitude,
        "longitude": longitude
    }

    message_json = json.dumps(message)
    mqttc.publish(TOPIC, message_json)
    time.sleep(5)
