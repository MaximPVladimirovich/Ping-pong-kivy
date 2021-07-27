from random import randint

import kivy
from Demos.mmapfile_demo import offset
from kivy.properties import NumericProperty, ReferenceListProperty, Clock, ObjectProperty
from kivy.vector import Vector

kivy.require('2.0.0')

# Base class of application inherits from App class
from kivy.app import App
from kivy.uix.widget import Widget


# paddle
class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            speedup = 1.1
            offset = 0.02 * Vector(0, ball.center_y-self.center_y)
            ball.velocity = speedup * (offset - ball.velocity)


# The game rules from pong.kv
class PingPong(Widget):
    ball = ObjectProperty(None)

    def serve_ball(self):
        self.ball.center = self.center
        self.ball.velocity = Vector(4, 0).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()

        # call ball.move and others
        # bounce off top and bottom
        if (self.ball.y < 0 ) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # bounce off left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1
        pass


# Ball
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
        game = PingPong()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    PongApp().run()
