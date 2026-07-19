# Inheritance

'''
Sub class of a main class.*
'''

class employee:
    def __init__(self, name , id):
        self. name = name
        self.id = id

    def showdetails(self):
        print(f"The name of employee: {self.id} and {self.name}")

class programmer(employee):
    def showlanguage():
        print("The default langugae is python")

e1 = employee('Rohan', 240)
e1.showdetails()

e2 = employee('Ron', 10)
e2.showdetails()

# Shows errpr cause it does not have those attributes and show language is not defined on Employee
# e2 = employee('Ron', 10)
# e2.showlanguage()

# this will work
# e2 = programmer('Ron', 10)
# e2.showlanguage()
# e2.showdetails()

e3 = employee('han', 40)
e3.showdetails()


'''
All the functions in the parent class can be workable with sub class, but functions of sub class will not work with main class

here employee can not work with showlanguage but programmer can work with showdetails.
'''

# Multiple types of inheritance:

