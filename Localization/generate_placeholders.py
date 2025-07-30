#!/usr/bin/env python3
import json

def print_all(dictionary, path_segments=[]):
    for key, value in dictionary.items():
        full_path_segments = [*path_segments, key]
        full_path_name = ".".join(full_path_segments)
        if isinstance(value, dict):
            print(f"{full_path_name:<70} {{")
            print_all(value, full_path_segments)
            print(f"{full_path_name:<70} }}")
        elif isinstance(value, str):
            print(f"{full_path_name:<70} | {repr(value)}")
        else:
            raise f"{full_path_name} has a weird value!!\nvalue: {value}\ntype: {type(value)}"

def placeholderify(dictionary, short_mode, path_segments=[]):
    for key, value in dictionary.items():
        full_path_segments = [*path_segments, key]
        full_path_name = ".".join(full_path_segments)
        if isinstance(value, dict):
            # print(f"{full_path_name:<70} {{")
            placeholderify(value, short_mode, full_path_segments)
            # print(f"{full_path_name:<70} }}")
        elif isinstance(value, str):
            # print(f"{full_path_name:<70} | {repr(value)}")
            if short_mode:
                dictionary[key] = f"${key}$"
            else:
                dictionary[key] = f"$${full_path_name}$$"
            # print(f"{full_path_name:<70} | {repr(value)}")
        else:
            raise f"{full_path_name} has a weird value!!\nvalue: {value}\ntype: {type(value)}"

with open("en-US.json") as f:
    translation_data = json.load(f)

    print_all(translation_data)

    with open("PLACEHOLDERS_LONG.json", "w+") as f2:
        placeholderify(translation_data, False)
        print_all(translation_data)
        json.dump(translation_data, f2)

    with open("PLACEHOLDERS_SHORT.json", "w+") as f3:
        placeholderify(translation_data, True)
        print_all(translation_data)
        json.dump(translation_data, f3)

