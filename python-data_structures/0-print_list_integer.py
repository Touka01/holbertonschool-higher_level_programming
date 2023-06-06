#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for num in my_list:
        print("{0}".format(num))

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
