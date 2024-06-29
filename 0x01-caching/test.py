#!/usr/bin/python3
"""
Test
"""
import sys

try:
    imported_file = __import__('3-lru_cache')
    if imported_file.__doc__ is None or len(imported_file.__doc__) < 10:
        print("No documentation found")
    else:
        print("OK")
except:
    print(sys.exc_info()[1])