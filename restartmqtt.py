import paho.mqtt.client as mqtt
import os

def on_connect(mosq, obj, rc):
    mqttc.subscribe("Proyector", 0)

def on_message(mosq, obj, msg):
    msg = str(msg.payload).lower()
    if msg in ["reset","restart","reebot","shutdown","turnoff","off"]:
        os.system("/sbin/shutdown -r now") 

def on_log(mosq, obj, level, string):
    print(string)


mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
#mqttc.on_publish = on_publish
# Connect
mqttc.connect("localhost", 1883,60)


# Continue the network loop
mqttc.loop_forever()
