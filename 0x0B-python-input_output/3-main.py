#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

my_list = [1, 2, 3]
s_my_list = to_json_string(my_list)
print(s_my_list)
print(type(s_my_list))

my_dict = { '1':23}
s_my_dict = to_json_string(my_dict)
print(s_my_dict)
print(type(s_my_dict))
