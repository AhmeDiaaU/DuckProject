from Behaviors.interfaces import IFlyBehavior


class FlyWithWings(IFlyBehavior):
    def fly(self):
        print("I'm flying with wings!")


class FlyNoWay(IFlyBehavior):
    def fly(self):
        print("I can't fly.")