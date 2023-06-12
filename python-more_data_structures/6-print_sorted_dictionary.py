#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None
    sort = sorted(a_dictionary)
    for element in sort:
        print("{}: {}".format(element, a_dictionary[element]))
