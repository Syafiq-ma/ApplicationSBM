import kivy

from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
import paho.mqtt.client as mqtt
from paho.mqtt import client as mqtt_client

def on_message(client, userdata, msg):
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
client = mqtt_client.Client("")
client.connect('broker.emqx.io', 1883)
client.subscribe('/sisberhok/esp/ipaddr')
client.on_message = on_message
client.loop_start()

class SensorBox(MDBoxLayout):
    pass


class Display(FloatLayout):
    def __init__(self) -> None:
        super().__init__()
        def on_connect(mqttc, userdata, rc):
            print("Connected with result code "+str(rc))
        def on_mesage(client, userdata, msg):
            print('f')
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        client = mqtt.Client("aas") 
        client.connect('broker.emqx.io', 1883)
        client.on_connect = on_connect
        client.subscribe("/sisberhok/esp/ipaddr")
        
    def toggle(self):
        client = mqtt.Client("aas") 
        client.connect('broker.emqx.io', 1883)
        client.publish("/sisberhok/esp/toggle")

class DisplayApp(App):
    def build(self):
        def on_message(client, userdata, msg):
            print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        
        client = mqtt_client.Client("")
        client.on_message = on_message
        client.connect('broker.emqx.io', 1883)
        client.subscribe('/sisberhok/esp/ipaddr')

        return Display()


if __name__ == '__main__':
   DisplayApp().run()