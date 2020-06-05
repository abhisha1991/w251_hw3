import paho.mqtt.client as mqtt
import time
import socket
import uuid

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
    # For this, we just store the image in the /data folder in the container. Why?
    # Because we mounted /data container folder with the /data host machine folder,
    # the saved files show up in /data in the host machine.
    # Further, because we connected /data on the host machine to ibm s3
    # any changes in /data on the host machine show up in ibm s3
    # Mounting command: s3fs abhihw3bucket $HOME/data -o url=https://s3.us-east.cloud-object-storage.appdomain.cloud -o passwd_file=$HOME/.cos_creds
    # Container start command: docker run -dit -v ~/data:/data --name test imgproc1
    file_name = "/data/" + str(uuid.uuid4())
    f = open(file_name, "w")
    f.write(message.payload)
    print("Wrote successfully to file ", file_name)
    f.close()

hostname = socket.gethostname()

print("creating a new client instance on host ", hostname)
client = mqtt.Client("P1")

client.on_connect = on_connect
client.on_message = on_message

print("connecting to broker")
client.connect("127.0.0.1", 1883, 60)

print("Starting a loop on the subscriber")
# start background daemon to loop forever and listen for that topic
client.loop_forever()
