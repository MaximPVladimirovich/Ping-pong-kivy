import kivy
kivy.require('2.0.0')

# Base class of application inherits from App class
from kivy.app import App
from kivy.uix.widget import Widget


class PingPong(Widget):
    pass


# Define base class of App
class PongApp(App):

    # Root widget
    def build(self):
        return PingPong()


if __name__ == '__main__':
    PongApp().run()
