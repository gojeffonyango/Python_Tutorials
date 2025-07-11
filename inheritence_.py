# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 15:02:51 2025

@author: gojef
"""

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Child class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Usage
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks.
