# getters and setters

# getter
class Myclass:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f"Value is {self._value}")

    @property
    def value(self):
        return self._value
    
obj = Myclass(10)
print(obj._value)
obj.show()

# setter
class Myclass:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f"Value is {self._value}")

    @property
    def value(self):
        return self._value
    
    @value.setter
    def ten_value(self, new_value):
        self._value = new_value/10
        
obj = Myclass(10)
print(obj._value)
obj.show()
