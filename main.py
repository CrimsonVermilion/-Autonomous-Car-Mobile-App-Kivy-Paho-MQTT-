import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import StringProperty
import json
import random
from paho.mqtt import client as mqtt_client

# Define the MQTT broker address and port
broker = 'broker.emqx.io'
port = 1883
mqtt_topic="mqtt/tasks_recieved"

#matrix defined to put the Xdist1 ydist1 xdist2 ydist2

dist_matrix = [[1,0,0,0,0,0],
               [2,0,0,0,0,0],
               [3,0,0,0,0,0],
               [4,0,0,0,0,0],
               [5,0,0,0,0,0],
               [6,0,0,0,0,0],
               [7,0,0,0,0,0],
               [8,0,0,0,0,0],
               [9,0,0,0,0,0],
               [10,0,0,0,0,0],
               [11,0,0,0,0,0]]

payload_data = {
                "task_id": str(random.randint(1, 2000)),
                "pickup_x": 1,
                "pickup_y": 2,
                "dropoff_x": 3,
                "dropoff_y": 4
                }
print(payload_data)
client_id = 'publish12-{}'.format(random.randint(0, 1000))
mqtt_client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)

# Connect to the MQTT broker
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code {}".format(rc))

    mqtt_client.on_connect = on_connect
    mqtt_client.connect(broker, port)





# Publish the payload on the outgoing topic
def publish_mqtt(mqtt_topic, msg):
    result = mqtt_client.publish(mqtt_topic, msg)
    status = result[0]
    if status == 0:
        print("Sent message to topic {}".format(mqtt_topic))
    else:
        print("Failed to send message to topic {}".format(mqtt_topic))   
        
        
class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    dist1 = ObjectProperty(None)
    dist2 = ObjectProperty(None)
   
    def btn(self):
        print("button is pressed")
        d1 = 0
        d2 = 0
        print(self.dist1.text , self.dist2.text)
        distination1 = float(self.dist1.text)
        distination2 = float(self.dist2.text)
        for i in range(11):
            if (dist_matrix[i][0] == distination1):
                print('you are right')
                payload_data["pickup_x"] = str(dist_matrix[i][1])
                payload_data["pickup_y"] = str(dist_matrix[i][2])
                d1 = 1  

            if (dist_matrix[i][0] == distination2):
                print('you are right')
                payload_data["dropoff_x"] = str(dist_matrix[i][1])
                payload_data["dropoff_y"] = str(dist_matrix[i][2])
                d2 = 1
        
                 
        print('we are out of deep IF')      
        print(d1)
        print(d2)    
        if( d1 == 1 ):
            print(payload_data)
            payload_json = json.dumps(payload_data)
            client= connect_mqtt()
            publish_mqtt(mqtt_topic, payload_json)        
            print('we exited the for loop')
            self.manager.current = 'fourth'
        else:
            print('you are wrong')
            self.manager.current = 'wrong'
       



class SignupWindow(Screen):
    pass


class ThirdWindow(Screen):
    pass


class FourthWindow(Screen):
    def start_timer(self):
        Clock.schedule_once(self.change_to_fifth, 2)

    def change_to_fifth(self, dt):
        self.manager.current = 'seventh'
    pass


class FifthWindow(Screen):
    pass


class SixthWindow(Screen):
    pass


class SeventhWindow(Screen):
    pass


class EighthWindow(Screen):
    def start_timer(self):
        Clock.schedule_once(self.change_to_ninth, 2)

    def change_to_ninth(self, dt):
        self.manager.current = 'ninth'
    pass


class NinthWindow(Screen):
    pass


class InfoWindow(Screen):
    per1 = ObjectProperty(None)
    per2 = ObjectProperty(None)
    pass
            
        



class WrongdisWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyApp(App):

    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()
