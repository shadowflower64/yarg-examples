#!/usr/bin/env python3
import base64

def create_line(section_name, ticks_since_last_event):
    encoded_thing = base64.b64encode(b'\xff\x01' + bytes(section_name, 'utf-8'))
    if " " in section_name:
        line = f"""
        <X {ticks_since_last_event} 0 0 0 1 "{section_name}"
          {encoded_thing.decode("utf-8")}
        >"""
    else:
        line = f"""
        <X {ticks_since_last_event} 0 0 0 1 {section_name}
          {encoded_thing.decode("utf-8")}
        >"""

    return line

with open("practice_section_list.txt") as f:
    sections = f.readlines()
    first_section = True
    final_output = ""
    for section_name in sections:
        if first_section:
            final_output += create_line(section_name.strip(), 3840)
            first_section = False
        else:
            final_output += create_line(section_name.strip(), 1920)

    print(final_output)
