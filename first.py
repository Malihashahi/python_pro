users ={
  "bahar":"1234",
  "maliha": "6854",
  "amir": "35333"
}


entered_username = input('enter your username :')
entered_password = input('enter your password :')
while entered_username not in users or users[entered_username] != entered_password:
  print('your username is worng')
  entered_username= input('enter your username again : ')
  entered_password= input('enter your password again')