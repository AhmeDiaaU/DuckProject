from Ducks.Duck import Duck
from Behaviors.fly_behaviours import FlyNoWay
from Behaviors.quack_behaviours import Squeak


class RubberDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()
    
    def display(self):
        return "I'm a rubber duck"