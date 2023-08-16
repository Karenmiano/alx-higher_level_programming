#!/usr/bin/python3
def no_c(my_string):
    s = ''
    for i in my_string:
        if i in 'cC':
            continue
        s += i
    return s
