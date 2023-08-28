#!/usr/bin/python3

def safe_print_list(my_list=[], x = 0):
    try:
        for t in range(x):
            print(my_list[t], end ="")
    except IndexError:
        x = t #updates the value of x to index reached before exception occurred
    finally:
        print()
        return x
