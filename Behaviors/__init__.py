
from Behaviors.interfaces import IFlyBehavior, IQuackBehavior
from Behaviors.fly_behaviours import FlyWithWings, FlyNoWay
from Behaviors.quack_behaviours import Quack, Squeak, MuteQuack

__all__ = [
    'IFlyBehavior', 'IQuackBehavior',
    'FlyWithWings', 'FlyNoWay',
    'Quack', 'Squeak', 'MuteQuack'
]