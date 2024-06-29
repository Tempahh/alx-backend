#!/usr/bin/python3
"""
Test
"""
import sys

try:
    BasicCache = __import__('0-basic_cache').BasicCache
    if BasicCache is not None:
        print("OK")
    else:
        print("0-basic_cache.py doesn't contain BasicCache")
except:
    print(sys.exc_info()[1])