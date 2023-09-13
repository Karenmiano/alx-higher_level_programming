#!/usr/bin/python3
"""Script that adds commandline arguments to a Python list
and saves the list to a file."""
if __name__ == '__main__':

    from sys import argv
    load_from_json_file = \
        __import__("6-load_from_json_file").load_from_json_file
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

    try:
        growing_list = argv[1:]
        growing_list += load_from_json_file("add_item.json")
        save_to_json_file(growing_list, "add_item.json")
    except FileNotFoundError:
        save_to_json_file(growing_list, "add_item.json")
