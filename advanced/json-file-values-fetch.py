import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# Convert the dictionary to a JSON string
json_str = json.dumps(x)

# Parse the JSON string back into a dictionary
data = json.loads(json_str)

# Access the list of cars and print the mpg values
for car in data["cars"]:
    print(car["mpg"])
