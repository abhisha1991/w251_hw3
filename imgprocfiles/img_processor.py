import paho.mqtt.client as mqtt
import time
import socket

def on_connect(client, userdata, flags, rc):
    print("Connected to broker with result code :", str(rc))
    client.subscribe("fdimages/#")
    print("Subscribed to topic fdimages/#")

def on_message(client, userdata, message):
    print("message received with length ", len(message.payload.decode("utf-8")))
    print("message topic = ", message.topic)
    print("message qos = ", message.qos)
    print("message retain flag = ", message.retain)
    send_to_storage(message)

def send_to_storage(message):
    print("sending message to object storage")
    # code for sending message

hostname = socket.gethostname()

print("creating a new client instance on host ", hostname)
client = mqtt.Client("P1")

client.on_connect = on_connect
client.on_message = on_message

print("connecting to broker")
client.connect("mqtt.eclipse.org", 1883, 60)

print("Starting a loop on the subscriber")
# start background daemon to loop forever and listen for that topic
client.loop_forever()
