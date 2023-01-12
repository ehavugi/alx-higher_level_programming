#!/usr/bin/python3

def uniq_add(my_list=[]):
    a = set(my_list)
    tot = 0
    for x in a:
        tot += x
    return tot
