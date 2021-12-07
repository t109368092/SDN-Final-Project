import paho.mqtt.client as mqtt
import json
import requests


def connect():
    task1 = {
        	"dpid": 1,
		"match":
		{
		"in_port": 1
		},
		"actions":
		[
			{
				"type":"OUTPUT",
				"port":2,
			}
		]
    	    }

    task2 = {
		"dpid": 1,
		"match":
		{
		"in_port": 2
		},
		"actions":
		[
			{
				"type":"OUTPUT",
				"port":1,
			}
		]
	    }

    task3 = {
		"dpid": 2,
		"match":
		{
		"in_port": 1
		},
		"actions":
		[
			{
				"type":"OUTPUT",
				"port":2,
			}
		]
	    }

    task4 = {
		"dpid": 2,
		"match":
		{
		"in_port": 2
		},
		"actions":
		[
			{
				"type":"OUTPUT",
				"port":1,
			}
		]
	    }

    resp1 = requests.post('http://127.0.0.1:8080/stats/flowentry/add', json = task1)
    resp2 = requests.post('http://127.0.0.1:8080/stats/flowentry/add', json = task2)
    resp3 = requests.post('http://127.0.0.1:8080/stats/flowentry/add', json = task3)
    resp4 = requests.post('http://127.0.0.1:8080/stats/flowentry/add', json = task4)

def dis_connect():
    task1 = {
        	"dpid": 1,
		"match":
		{
		"in_port": 1
		},
		"actions":
		[
			{
				"type":"OUTPUT",
				"port":2,
			}
		]
    	    }

    task2 = {
		"dpid": 1,
		"match":
		{
		"in_port": 2
		},
		"actions":
		[
			{
				"type":"OUTPUT",
				"port":1,
			}
		]
	    }

    task3 = {
		"dpid": 2,
		"match":
		{
		"in_port": 1
		},
		"actions":
		[
			{
				"type":"OUTPUT",
				"port":2,
			}
		]
	    }

    task4 = {
		"dpid": 2,
		"match":
		{
		"in_port": 2
		},
		"actions":
		[
			{
				"type":"OUTPUT",
				"port":1,
			}
		]
	    }

    resp1 = requests.post('http://127.0.0.1:8080/stats/flowentry/delete', json = task1)
    resp2 = requests.post('http://127.0.0.1:8080/stats/flowentry/delete', json = task2)
    resp3 = requests.post('http://127.0.0.1:8080/stats/flowentry/delete', json = task3)
    resp4 = requests.post('http://127.0.0.1:8080/stats/flowentry/delete', json = task4)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    connect()

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("tempandhumi")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    # print(msg.topic+" "+str(msg.payload))
    temp = str(msg.payload.decode())
    print("Temperature:" + " " + str(msg.payload.decode()))
    if temp >= '25':
        print("action")
        dis_connect()

    
    with open('temperature.csv', 'w') as f:
        f.write(str(msg.payload))   

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.50.108", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
