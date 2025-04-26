class Student:
    def __init__(self):
        self._name = None
        self._age = None
        self.subjects = []


    def do_something(self):
        pass
    
    @property
    def name(self):
        return self._name

    @name.setter  # noqa: F821
    def name(self, value): # obj.name = V
        if not self._name:
            self._name = value
            if not isinstance(self._name, str):
                raise TypeError(f'{self._name} should be string')
        
    
    @name.deleter # del name
    def name(self):
        print('delete internal variable _name.')
        del self._name

import time
import math

def time_calculation(func):
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func()
        end = time.time()
        
        print(f'time taken: {end - start:.2}')
        
        return result
        
    return wrapper

@time_calculation
def sayhello(k=1):
    print("Hello world")


s = Student()
s.name = 'Hu'

del s.name

print(type("balsada"))