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
mqtt_client = mqtt_client.Client('publish-{}'.format(random.randint(0, 1000)))


class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    dist1 = ObjectProperty(None)
    dist2 = ObjectProperty(None)
    
    def btn(self):
        print("button is pressed")
        print(self.dist1.text , self.dist2.text)
        distination1 = float(self.dist1.text)
        distination2 = float(self.dist2.text)
        for i in range(11):
            if (dist_matrix[i][0] == distination1):
                print('we are in deep IF')
                payload_data["pickup_x"] = str(dist_matrix[i][1])
                payload_data["pickup_y"] = str(dist_matrix[i][2])

            if (dist_matrix[i][0] == distination2):
                print('we are in deep IF')
                payload_data["dropoff_x"] = str(dist_matrix[i][1])
                payload_data["dropoff_y"] = str(dist_matrix[i][2])
                
        print(payload_data)
        payload_json = json.dumps(payload_data)        
        print('we exited the for loop')
       



class ThirdWindow(Screen):
    pass


class FourthWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()
