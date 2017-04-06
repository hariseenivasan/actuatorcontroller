import paho.mqtt.client as mqtt
import json,math,ConfigParser

SUBSCRIBE_TOPIC = "readings/temperature"
STATUS_TOPIC_ = "actuators/room-"

configParser = ConfigParser.RawConfigParser()   
configFilePath = r'service.config'
	
def on_connect(client, userdata, rc):
	print("Connected with result code "+str(rc))
	client.subscribe(SUBSCRIBE_TOPIC)
	
def on_message(client, userdata, msg):
	topic = msg.topic

	m=json.loads(msg.payload)
	obtainedvalue=m["value"]
	sensorID = m["sensorID"]
	roomNumber = sensorID.split("-")[-1]
	#We believe the algorithm to calculate the actuator openess is directly proportional to the positive diffrences in value otherwise 0
	tempvalue = int(configParser.get('default-values','tempvalue'))
	valuetoSet = obtainedvalue-tempvalue
	if valuetoSet<0:
		valuetoSet = 0
	elif valuetoSet>tempvalue:
		valuetoSet = tempvalue
	percentActuatorOpen = int((valuetoSet/tempvalue)*100)
	statusTopic = STATUS_TOPIC_+roomNumber
	client.publish(statusTopic, json.dumps({ "level":percentActuatorOpen}))
	
def getServiceNode():
	configParser.read(configFilePath)
	propertySection = 'default-network'	
	hostname = "192.168.99.100"#str(configParser.get(propertySection,'hostname'))
	port = int(configParser.get(propertySection,'port'))
	keepalive = int(configParser.get(propertySection,'keepalive'))
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(hostname,  port, keepalive)
	client.loop_forever()

getServiceNode()
'''
Singleton Class for future design, while implementing queue fasion then any kind of service reconnection will lose the data.
class GetMQTTService(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(GetMQTTService, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MQTTService(object):
    __metaclass__ = GetMQTTService
'''