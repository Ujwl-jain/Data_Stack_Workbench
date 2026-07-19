# Acces Modifiers

'''
Python do not have a public, private, protected type of variables, just like otehr languages

But we still use it but in different ways, like:

by defaul all varibles are public, they are used to limit the access of class variable and class methods outside of the class
while implementing the concepts of inheritance.

These are just convention
types:

Public, private, protected
'''

# public:
'''
using a sample program we can access the variable from outside the class, private can not do

Below we are able to access the name in the class from outside the class
'''
class employee:
    def __init__(self):
        self.name = 'harry'

a = employee()
print(a.name)


# private
'''
we can not access the variable in class from the outside of class.

private variable = __ name, using __(double underscore) it is declared or indicator as private
below we can not access from outside of class, but we can do it, using name mangaling

access the vairable using: _ following the name of the class and then the variable : 
'''
class employee:
    def __init__(self):
        self.__name = 'harry'

a = employee()
# print(a.__name) can not be accessed directly
print(a._Emplpoyee__name) # that is how we can access the private variable


# Protected
'''
it can be accessed in the class and sub class only, no outisde. 

protected variable use the indicator: _name

no need to do name mangaling here, can directly access it,
'''

class student:
    def __init__(self):
        self._name = 'harry'

    def _funName(self): # protected variable or method
        return 'Code with harry'
    
class subject(student): #inherit class
    pass

obj = student()
obj1 = subject()


# calling by object of student class
print(obj._name)
print(obj._funName())

# calling by object of subject class
print(obj1._name)
print(obj1._funName())


'''
Lastly python wont force these access modifiers, these are just conventions we can use to act as private and protected
it is better to use the protected one as private though, otherwise we need to do mangaling
'''