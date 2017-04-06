import paho.mqtt.client as mqtt
import json,random,time
SUBSCRIBE_TOPIC_ = "actuators/room-"
PUBLISH_TOPIC = "readings/temperature"
SVC_HOST_NAME = "192.168.99.100"
SVC_PORT = 1883

def on_message():
	print "Topic: ", msg.topic+'\nMessage: '+str(msg.payload)
	m=json.loads(msg.payload)
	print m["level"]	
def testSendSensorValue(sensorID):
	sensorID=str(sensorID)
	mqttc = mqtt.Client("Test_Sensor_"+sensorID)
	mqttc.on_message = on_message
	mqttc.subscribe(SUBSCRIBE_TOPIC_+sensorID)
	mqttc.connect(SVC_HOST_NAME, SVC_PORT)

	m={
	  "sensorID": "sensor-"+sensorID,
	  "type": "temperature",
	  "value": random.uniform(0, 50)
	}

	mqttc.publish(PUBLISH_TOPIC, json.dumps(m))
	mqttc.loop(200) #timeout = 2s
	
	
#def getListnerNode():
for i in range(1,100):
	testSendSensorValue(1)
	time.sleep(random.randint(0,10))