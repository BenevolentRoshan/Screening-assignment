# Abstract class: If it contains an asbtrcat method.
# Abstract Method: Method has declaration but no definition
# Decorator: special functions which adds additional functionality to an existing function or code.

# importing abstract base class(ABC)
from abc import ABC, abstractmethod

#Abstract Class
class employee(ABC):
    @abstractmethod                 # Decorator
    def details(self):              # Abstract Method
        pass

    @abstractmethod
    def show(self):
        pass
# concrete class
class employees(employee):
    def details(self):
        print("employees Details")
    def show(self):
        print("Show details")

roshan=employees()
roshan.details()
roshan.show()
