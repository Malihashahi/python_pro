users ={
  "bahar":"1234",
  "maliha": "6854",
  "amir": "35333"
}


entered_username = input('enter your username :')
entered_password = input('enter your password :')
if entered_username in users and users[entered_username]== entered_password:
  print('yes your welcome')
else:
  print('your not our users')