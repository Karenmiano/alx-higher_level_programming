#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_result = []
    for i in range(list_length):
        try:
            list_result.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            list_result.append(0)
        except ZeroDivisionError:
            print("division by zero")
            list_result.append(0)
        except IndexError:
            print("out of range")
            list_result.append(0)
        finally:
            continue
    return (list_result)
