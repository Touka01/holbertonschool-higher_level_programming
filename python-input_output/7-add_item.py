#!/usr/bin/python3
"""
Module 7-add_item

Contains function that adds and saves to Python obj to JSON file; loads objects

# run with ./7-add_item.py
#
# cat add_item.json ; echo ""
# expect output: []
#
# ./7-add_item.py some random args
# cat add_item.json ; echo ""
# expect output: ["some", "random", "args"]

"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""script that adds all arguments to a Python list"""

file = "add_item.json"
json_list = []

if os.path.exists(file):
    json_list = load_from_json_file(file)

for i in range(1, len(sys.argv)):
    json_list.append(sys.argv[i])

save_to_json_file(json_list, file)
