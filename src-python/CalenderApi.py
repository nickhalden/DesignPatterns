from abc import ABC, abstractmethod
import time


class Event(ABC):
    def __init__(self, name, e):
    def createEvent(self, name, date, time):
    pass


class CalenderEvent:
    pass

class MeetingEvent:
    pass

class InterviewEvent:
    pass




class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        print("Some implementation!")


class AnotherSubclass(AbstractClassExample):


    def do_something(self):
     super().do_something()
     print("The enrichment from AnotherSubclass")


x = AnotherSubclass()
x.do_something()



