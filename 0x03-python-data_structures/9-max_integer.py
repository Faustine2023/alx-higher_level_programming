#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    Int_Max = my_list[0]
    for o in my_list:
        if o > Int_Max:
            Int_Max = o
    return Int_Max
