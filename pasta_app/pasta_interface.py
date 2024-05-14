from abc import ABC, abstractmethod

class Pasta(ABC):
    @abstractmethod
    def set_sauce(self, sauce):
        pass

    @abstractmethod
    def set_topping(self, topping):
        pass

    @abstractmethod
    def set_dressing(self, dressing):
        pass

    @abstractmethod
    def get_details(self):
        pass
