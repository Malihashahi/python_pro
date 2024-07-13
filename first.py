import json

# some JSON:
x =  '{ "name":"bahar", "age":23, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])