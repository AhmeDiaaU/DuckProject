from Ducks.Duck import Duck
from Behaviors.fly_behaviours import FlyWithWings
from Behaviors.quack_behaviours import Quack


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()
    
    def display(self):
        return "I'm a real Mallard duck"