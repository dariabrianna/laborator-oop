from abc import ABC, abstractmethod

class Stack(ABC):
    @abstractmethod
    def push(self, item):
        pass
    
    @abstractmethod
    def pop(self):
        pass
    
    @abstractmethod
    def peek(self):
        pass
    
    @abstractmethod
    def is_empty(self):
        pass
    
    @abstractmethod
    def is_full(self):
        pass
    
    @abstractmethod
    def size(self):
        pass
