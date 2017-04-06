import paho.mqtt.client as mqtt
import json
from time import gmtime, strftime


def on_connect(client, userdata, rc):
	client.subscribe("actuators/room-1")

def on_message(client, userdata, msg):
	m=json.loads(msg.payload)
	dttime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

	print dttime+ "# Setting Level to " + str(m["level"])+"%"
	
	

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.99.100", 1883, 60)
client.loop_forever()