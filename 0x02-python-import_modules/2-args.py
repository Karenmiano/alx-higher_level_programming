#!/usr/bin/python3
if __name__ == '__main__':
    """Reflects the command line arguments passed to itself"""
    from sys import argv
    args = len(argv) - 1
    if args == 0:
        print("0 arguments.")
    elif args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args))
    index = 1
    for j in argv[1:]:
        print("{}: {}".format(index, j))
        index += 1
