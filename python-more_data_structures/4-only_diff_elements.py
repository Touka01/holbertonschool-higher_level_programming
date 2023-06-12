#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = set()
    count = 0
    for i in set_1:
        for j in set_2:
            if i != j:
                count = count + 1
        if count == len(set_2):
            diff.add(i)
        count = 0
    for i in set_2:
        for j in set_1:
            if i != j:
                count = count + 1
        if count == len(set_1):
            diff.add(i)
        count = 0
    return (diff)
