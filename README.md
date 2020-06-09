# w251_hw3 by abhisha@berkeley.edu

This project covers home work 2 for class w251: https://github.com/MIDS-scaling-up/v2/tree/master/week03/hw

The project consists of 4 folders:
1. fdfiles contains the files necessary for the face detector module that runs on the TX2 module
2. fwderfiles contains the files necessary for the forwarding module that receives data from the face detector via the mosquitto broker and forwards it to the remote ibm cloud vsi
3. imgprocfiles contains the files necessary for the image processor module that runs in the ibm cloud vsi and sends data to ibm storage
4. images contains some sample result images of cropped faces in black and white

The general pattern to run any of the sub folders is as follows:
1. build the docker image for the module
2. launch the containers for the module
3. Each module has an instructions.txt that explains step by step on how to reproduce the results in each module

Note that the pre requisites to run the project imply that the user must have a jetson tx2 and a usb camera.

Note that we can choose to use the alpine broker by creating our own broker or we can use an off the shelf broker like eclipse-mosquitto

Also note that the QOS and topics have been explained in the doc: topics_qos_explanation.txt
