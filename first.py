thistuple = ("apple", "banana", "cherry")
print(thistuple)


thistuple2 = ("apple", "banana", "cherry")
print(thistuple2[1])


thistuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple3[2:5])


thistuple4 = ("apple", "banana", "cherry")
y = list(thistuple4)
y.append("orange")
thistuple4 = tuple(y)

thistuple5 = ("apple", "banana", "cherry")
for i in range(len(thistuple5)):
  print(thistuple5[i])

  tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

