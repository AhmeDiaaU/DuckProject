from abc import ABC, abstractmethod
import io
import sys

from Behaviors.interfaces import IFlyBehavior, IQuackBehavior


class Duck(ABC):
    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None
    
    def set_fly_behavior(self, fb):
        self.fly_behavior = fb
    
    def set_quack_behavior(self, qb):
        self.quack_behavior = qb
    
    def perform_fly(self):
        # Redirect stdout to capture the output
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        
        self.fly_behavior.fly()
        
        # Get the output and restore stdout
        output = new_stdout.getvalue()
        sys.stdout = old_stdout
        
        return output
    
    def perform_quack(self):
        # Redirect stdout to capture the output
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        
        self.quack_behavior.quack()
        
        # Get the output and restore stdout
        output = new_stdout.getvalue()
        sys.stdout = old_stdout
        
        return output
    
    def swim(self):
        return "All ducks float, even decoys!"
    
    @abstractmethod
    def display(self):
        pass