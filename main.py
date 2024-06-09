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
from os import listdir



class MainWindow(Screen):
    pass


class SecondWindow(Screen):
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


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()
