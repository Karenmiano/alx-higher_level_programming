#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    evens = []
    for i in my_list:
        evens.append(True if i % 2 == 0 else False)
    return evens
