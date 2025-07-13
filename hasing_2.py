# -*- coding: utf-8 -*-
"""
Created on Sun Jul 13 22:05:21 2025

@author: gojef
"""

class CustomObject:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value) * 31  # Custom hash logic

obj = CustomObject("Hello")
print(f"Custom Hash: {hash(obj)}")
