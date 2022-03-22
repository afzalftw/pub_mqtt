import paho.mqtt.client as mqtt
sub_client = mqtt.Client()
sub_client.connect('broker.hivemq.com',1883)
print('Broker connected')
sub_client.subscribe('B19')
def notification(sub_client,userdata,msg):
    print(msg.payload)
sub_client.on_message = notification 
sub_client.loop_forever()