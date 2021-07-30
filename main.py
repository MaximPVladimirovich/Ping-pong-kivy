import kivy
from kivy.properties import NumericProperty, ReferenceListProperty, Clock, ObjectProperty
from kivy.vector import Vector
from kivy.core.audio import Soundloader

kivy.require('2.0.0')

# Base class of application inherits from App class
from kivy.app import App
from kivy.uix.widget import Widget


# paddle
class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            # Initialize vx, vy from the ball velocity
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


# Ball
class PongBall(Widget):
    # velocity of the ball on the x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # This moves the ball widget
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


# The game rules from pong.kv
class PingPong(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def on_touch_move(self, touch):
        # If user presses on paddle side it will move with mouse
        # For two player duplicate code below for player1
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

    def serve_ball(self, vel=(3.3, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # paddle bounce
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce off top and bottom
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # bounce off left and right
        # went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))


# Define base class of my application
class PongApp(App):

    # Instance of the root widget
    def build(self):
        game = PingPong()
        game.serve_ball()
        # Calls update function 60 times per second
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()
