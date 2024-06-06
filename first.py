#...................union ..............
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
#//////////////join set with tuple///////////////////////////////
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
#/////////////////intersection &//////////////////////////////////\
set5 = {"apple", "banana", "cherry"}
set6 = {"google", "microsoft", "apple"}

set7 = set1.intersection(set6)
print(set7)

#........../////////difference - ///////////////////..................
set8 = {"apple", "banana", "cherry"}
set9 = {"google", "microsoft", "apple"}

set10= set8.difference(set9)

print(set10)
