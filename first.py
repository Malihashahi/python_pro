#..........................................use pop .............
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#,,,,,,,,,,.....pop item method....................
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1.popitem()
print(thisdict1)
#..................del method usage...........................
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict2["model"]
print(thisdict2)
#.......................clear method................................
thisdict3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict3.clear()
print(thisdict3)