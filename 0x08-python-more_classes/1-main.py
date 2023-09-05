#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(hex(id(my_rectangle)))
my_rectangle2 = Rectangle(2, 4)
print(hex(id(my_rectangle2)))

