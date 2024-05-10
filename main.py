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
from paho.mqtt import client as mqtt_client


# Define the MQTT broker address and port
broker = 'broker.emqx.io'
port = 1883
mqtt_topic="mqtt/tasks_recieved"
username = ''
password = ''



class MainWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


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



def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code {}".format(rc))
    
    # Create a MQTT client instance
    mqtt_client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1,'publish-{}'.format(random.randint(0, 1000)))
    mqtt_client.username_pw_set(username, password)
    mqtt_client.on_connect = on_connect
    mqtt_client.connect(broker, port)




if __name__ == "__main__":
    MyApp().run()
