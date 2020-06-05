import paho.mqtt.client as paho
import time

broker = "10.28.81.61"
port = 1883

def on_publish(client,userdata,result):
    print("data published")

client1 = paho.Client("P1")
client1.on_publish = on_publish
client1.connect(broker, port)

while (True):
    time.sleep(5)
    ret = client1.publish("fdimages/test","hello-world")
    print("sent data!")
