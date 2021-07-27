import kivy
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

kivy.require('2.0.0')

# Base class of application inherits from App class
from kivy.app import App
from kivy.uix.widget import Widget


class PingPong(Widget):
    pass


class PongBall(Widget):
    # velocity of the ball on the x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


# Define base class of App
class PongApp(App):

    # Root widget
    def build(self):
        return PingPong()


if __name__ == '__main__':
    PongApp().run()
