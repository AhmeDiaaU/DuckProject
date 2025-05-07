from abc import ABC, abstractmethod


class IFlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


class IQuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass