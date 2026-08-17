# Constructors

'''
IT USED TO CREATE OBJECTS

2 types of constructor : default and parameterized
'''

# Normally we can do this
class person2:
  name  = "Harry"
  occupation = "SD"
  worth = 10
  def info(self):
    print(f"{self.name} is a {self.occupation}")


b = person2()
b.name = 'Shubh'
b.occupation = 'Manager'
b.info()

# But using constructor(parameterized)
class person2:
  def __init__(self,n,o):
    # below line will be printed everytime class is being called in the object
    print('Hi i am a person')
    # so using the same benefit above  we can do this,
    self.name = n
    self.occupation = o

  def info(self):
    print(f"{self.name} is a {self.occupation}")


b = person2('Harry', 'Developer')
# c = person2()  # <- show erro, no arguments pass, it is necessary to pass the default arguments in case of init function

# if we uncomment this then it will replace the arguments inside the object where class is called, in this case you can say arguments inside an object are default arguments where it is passed if no other info is passed for that object
# b.name = 'Shubh'
# b.occupation = 'Manager'

# Being called with particular arguments
b.info()

'''
See construtore workflow

it works in 2 ways

its like function, In classes whenever an object called a class and gave the arguments then it will pass the argument
in the class init method, from that self is automatized as object which is being called n is for harry and O is for developer

and then self will take those values in the info function to print the info further
'''

#  Default construtor
class person2:
  def __init__(self):
    # below line will be printed everytime class is being called in the object
    print('Hi i am a person')

  def info(self):
    print(f"{self.name} is a {self.occupation}")


b = person2()
b.name = 'Shubh'
b.occupation = 'Manager'
b.info()