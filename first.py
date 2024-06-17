name = input('enter your name : ')
name=name.lower()
name=name.replace(" ","")
b= []
for  n in name:
  if n not in b:
    print(f"your name has {name.count(n)} {n}")
    b.append(n)