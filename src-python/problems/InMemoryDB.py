from abc import ABC, abstractmethod
import time

class Entry(ABC):

    def __init__(self, value):
            self.value = value
            self.protected = None
            self.Directory = None
            self.parent = None;
            self.created = None;
            self.lastUpdated = None;
            self.lastAccessed = None

    super().__init__()

    @abstractmethod
    def Entry(self, name, directory):
        created = time.mktime()
        lastUpdated =time.localtime()
        lastAccessed = time.localtime()
    pass


    """ implemented by the caller"""
    @abstractmethod
    def size(self, name, directory):
        pass



    def delete(self):
        if self.parent == None:
            return
        else:
            print('method not implemented')



    # """write getter setters for all the methods"""




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

my_dict = {'name':'Jack', 'age': 26}

print (my_dict['name'])
