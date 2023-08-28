#!/usr/bin/python3
def safe_print_division(c, b):
    try:
        answer = c / b
    except (ZeroDivisionError, FloatingPointError):
        answer = None
    finally:
        print("Inside result: {}".format(answer))
    return answer
