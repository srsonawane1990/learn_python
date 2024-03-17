# The json library allows you to easily work with JSON-formatted data. You can use
# json.loads() to convert a JSON string into a Python dictionary and json.dumps() to
# convert a Python object back to a JSON string.

import json

f = open("xyx.json", "r")
data = json.load(f)

print(data)
print(data["c"])

