#!/usr/bin/python3
def magic_calculation(y, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > y:
                raise Exception('Too far')
            else:
                result += y ** b / i
        except Exception:
            result = b + y
            break
    return result
