#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    keys = list(a_dictionary)
    key_max = keys[0]
    for key in a_dictionary:
        if a_dictionary[key] > a_dictionary[key_max]:
            key_max = key
    return key_max
