[print("h"), print("i")]
class ParentClass:
    def __init__(self):
        print("Parent")

    def parent_method(self):
        print("This is a method from the parent class")

class ChildClass(ParentClass):
    def __init__(self):
        print("child")
        ParentClass().__init__()
    def child_method(self):
        print("This is a method from the child class")
        
    def call_parent_method(self):
        self.parent_method()  # Calling the parent class method

# Create an instance of the child class
child_instance = ChildClass()
child_instance.__init__()
# Calling methods from both child and parent classes
#child_instance.child_method()      # Calls child_method from ChildClass
#child_instance.call_parent_method() # Calls parent_method from ParentClass
