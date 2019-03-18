#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

# Number of contributed users

def get_user(element):       
    return element.get("uid")

def process_map(filename):
    users = []
    for _, element in ET.iterparse(filename):
        if element.tag == "node" or element.tag == "relation" or element.tag == "way":
            e = get_user(element)
            if e in users:
                continue
            else:
                users.append(e)
    return users

def test():
    users = process_map('sample.osm')
    pprint.pprint(len(users))

if __name__ == "__main__":
    test()