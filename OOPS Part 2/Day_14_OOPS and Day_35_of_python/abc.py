
from abc import ABC, abstractmethod

class Device(ABC):

    @abstractmethod
    def calculator(self):
        pass
    
    @abstractmethod
    def video(self):
        pass

class Mobile(Device):

    def calculator(self):
        print('\nCalculating complex equations.')

    def video(self):
        print('Making a video of a birthay party.\n')

class Laptop(Device):

    def calculator(self):
        print("\nHey! I'm a Laptop and I can also Calculate complex equations.")

    def video(self):
        print("You can also make video calls using me.\n")


realme = Mobile()
hp = Laptop()

realme.calculator()
realme.video()
hp.calculator()
hp.video()


        

