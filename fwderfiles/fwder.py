print("Starting the forwarder module...")
import paho.mqtt.client as mqtt
import time
import socket

def on_connect(client, userdata, flags, rc):
    print("Connected to broker with result code :", str(rc))
    client.subscribe("fdimagestx2/#")
    print("Subscribed to topic fdimagestx2/#")

def on_message(client, userdata, message):
    print("message received with length ", len(message.payload.decode("utf-8")))
    print("message topic = ", message.topic)
    print("message qos = ", message.qos)
    print("message retain flag = ", message.retain)
    republish_to_remote(message)

def on_publish_remote(client, userdata, result):
    print("data published")

def republish_to_remote(message):
    print("sending message to remote broker")
    # For this, we just republish the same message to the remote broker
    hostname = socker.gethostname()
    print("creating a new publisher client instance on host", hostname)
    client2 = mqtt.Client("P1")
    client2.on_publish = on_publish_remote
    client2.connect("50.22.169.235", 1883)
    client2.publish("fdimages/test", bytes(message))
    print("sent data remote!")

hostname = socket.gethostname()
print("creating a new subscriber client instance on host ", hostname)
client = mqtt.Client("P1tx2")

client.on_connect = on_connect
client.on_message = on_message

print("connecting to broker")
client.connect("127.0.0.1", 1883, 60)

print("Starting a loop on the subscriber")
# start background daemon to loop forever and listen for that topic
client.loop_forever()
