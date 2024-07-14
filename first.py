import json

# a Python object (dict):
x = {
  "name": "Maliha",
  "age": 24,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)