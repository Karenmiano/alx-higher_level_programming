#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while x:
            print(my_list[i], end="")
            x -= 1
            i += 1
    except IndexError:
        pass
    print()
    return (i)
