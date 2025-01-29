from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

class ChatScreen(Screen):
    pass

class ChatApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ChatScreen(name="chat"))
        return sm

if __name__ == "__main__":
    ChatApp().run()
