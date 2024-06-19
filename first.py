def passvalidation(password):
  if len(password)< 8:
     print("your password must be at least 8 character ")
  elif password.isnumeric():
     print("your password must have at least one letter ")
  elif password.isalpha():
     print("your password must have at least one number ")
  else:
     print("yes your password is correct ")


while True:
  password = input('enter your password : ')
  passvalidation(password)