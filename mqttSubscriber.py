import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("iotcourse/channel")

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    retain_string = "False"
    if msg.retain:
        retain_string = "True"
    print(msg.topic+" " + str(msg.payload) + " quality of service: " +
          str(msg.qos) + " retain attribute: " + str(retain_string))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)

client.loop_forever()
