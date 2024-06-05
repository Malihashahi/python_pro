thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#//////////////////////////////////////////////////
thisset1 = {"apple", "banana", "cherry"}

for x in thisset1:
  print(x)
  #/////////////////////////////////////////////////
  thisset2 = {"apple", "banana", "cherry"}

thisset2.add("orange")

print(thisset2)
#/////////////////////////////////////////////
thisset3 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset3.update(tropical)

print(thisset3)
#//////////////////////////////////////////////
thisset4 = {"apple", "banana", "cherry"}

thisset4.remove("banana")

print(thisset4)
#//////////////////////////////////////////////////////
thisset5 = {"apple", "banana", "cherry"}

thisset5.discard("banana")

print(thisset5)
#///////////////////////////////////////////
thisset6 = {"apple", "banana", "cherry"}

x = thisset6.pop()

print(x)

print(thisset6)
#//////////////////////////////////////////////////
thisset7 = {"apple", "banana", "cherry"}

thisset7.clear()

print(thisset7)
#///////////////////////////////////////////////
thisset8 = {"apple", "banana", "cherry"}

del thisset8

print(thisset8)

