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
    print("data published remotely")

def republish_to_remote(message):
    print("sending message to remote broker")
    # For this, we just republish the same message to the remote broker
    client2.publish("fdimages/test", bytes(message))
    print("sent data remote!")

hostname = socket.gethostname()
print("creating a new subscriber and re-publisher client instance on host ", hostname)

client = mqtt.Client("P1tx2")
client.on_connect = on_connect
client.on_message = on_message

client2 = mqtt.Client("P1")
client2.on_publish = on_publish_remote

print("connecting to broker on subscriber client")
# note that because we have added the fwder on the same network bridge as broker
# we can give the container name of the broker in the connection address
client.connect("mosquitto1", 1883, 60)

print("connecting to broker on remote cloud vm")
# ip of the remote vm can potentially change, bad practice to hard code
client2.connect("50.22.169.235", 1883, 60)

print("Starting a loop on the subscriber")
# start background daemon to loop forever and listen for that topic
client.loop_forever()
