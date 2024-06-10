i = 1
while i < 6:
  print(i)
  if i == 3:
    break

  k = 0
while k< 6:
  k += 1
  if i == 3:
    continue
  print(k)