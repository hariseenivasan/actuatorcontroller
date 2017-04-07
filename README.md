# actuatorcontroller
An MQTT based Controller and client which talks to each other to control the temperature based on the message received in the respective topic.

# Aim
Periodically Monitor the readings on topic "readings/temperature" in a json format
```json
{
  "sensorID": "sensor-1",
  "type": "temperature",
  "value": 25.3
}
```
And Output a relevent openess level to the topic "actuators/room-1"  
```json
{
  "level": 14
}
```

# Files
This example consists of 3 files
1. service_node.py: Services multiple room's actuators based on the above json's sensor id.
  It does this by subscribing to topic "readings/temperature" and accoring to the obtained json publishes to topic "actuators/room-#" depending on sensor ID.
2. test_service.py: Tests the service by sending time variant, dynamically generated sensor temperature data to topic "readings/temperature"
3. test_room1.py: Just subscribes for messages to topic "actuators/room-1" in order to print the level of openess obtained.

# Run 
Start both service_node.py and test_room1.py
Now run test_service.py to see test_room1 dumping the openess level depending on the random values sent to the service_node.

# Future Work
1. Consolidate the test file into one.
2. Design Queue based service_node.py for synchronized subscription or message publishing.
3. Left out on the actual algorithm for climate control, this depends on various other factors such as heater/cooler's rate for a given volume of room etc.
4. Thus, add other factors for calculation and modify the json inorder to make the service much more reliable.
5. Decouple on_message as generic serializable functions to be able to be passed into a queue design. (Handles multiple sensor data in a very optimized way)
6. Create a lambda to manage micro fucntions to handle various json.
7. Improve scalable design to monitor various sensors in rooms using a map file or map settings.
