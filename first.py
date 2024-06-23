
def myfunc(name):
  ups=0
  lows=0
  for n in name:
    if n.isupper():
         ups += 1
    elif  n.islower():
         lows += 1
    else: 
         pass
       
  print(f"upper cases: {ups}")
  print(f"lower cases: {lows}")



name = input('enter your name : ')
myfunc(name)