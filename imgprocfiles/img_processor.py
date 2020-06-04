import paho.mqtt.client as mqtt
import time
import socket

def on_message(client, userdata, message):
    print("message received with length", len(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)
    send_to_storage(message)

def send_to_storage(message):
    print("sending message to object storage")
    # code for sending message

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

broker_address= str(ip_address)

print("creating a new client instance")
client = mqtt.Client("P1")
client.on_message = on_message
print("connecting to broker")
client.connect(broker_address)

print("Subscribing to topic", "faceimages/#")
client.subscribe("faceimages/#")

# start background daemon to loop forever and listen for that topic
client.loop_forever()
