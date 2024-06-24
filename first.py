def  converter(day,month, year):
     if month > 10 or day  > 10 and month == 10:
          birthday = year + 622
     else:
          birthday = year + 621

     print(f"your year of birthday is {birthday}")    


day = int (input("enter day: "))
month = int (input("enter month: "))
year = int (input("enter year: "))

converter(day ,month , year)