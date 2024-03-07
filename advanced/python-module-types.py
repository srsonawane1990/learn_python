#Types of Python Modules
#There are two types of python modules:

#Built-in python modules
#User-defined python modules

# Example using the os module

import os

print(os.getcwd())
print(os.listdir())

# Example using the sys module

import sys

print(sys.version)
print(sys.argv)

# Example using the math module

import math

print(math.pi)
print(math.sin(math.pi / 2))

# Example using the json module

import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

json_data = json.dumps(data)
print(json_data)

# Example using the datetime module

import datetime

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

# Example using the re module

import re

text = "The quick brown fox jumps over the lazy dog."

result = re.search(r"fox", text)
print(result.start(), result.end(), result[0])

# Example using the random module

import random

print(random.randint(1, 100))
print(random.choice([1, 2, 3, 4, 5]))
