from Ducks.Duck import Duck
from Behaviors.fly_behaviours import FlyWithWings
from Behaviors.quack_behaviours import MuteQuack
class RocketDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()  # Could use RocketFlyBehavior if available
        self.quack_behavior = MuteQuack()   # Silent because it's focused on flying 😄

    def display(self):
        return "I'm a rocket-powered duck!"