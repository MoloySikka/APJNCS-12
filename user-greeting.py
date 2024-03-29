time = input("Enter the time (24 hour format e.g. 13:26): ")
time_list = time.split(":")
hours = int(time_list[0])
minutes = int(time_list[1])

if -1 < hours < 25 and -1 < minutes < 61:
  if hours < 12:
    print("Good morning!")
  elif hours < 17:
    print("Good afternoon!")
  elif hours < 20:
    print("Good evening!")
  elif hours < 25:
    print("Good night!")
else:
  print("Invalid!")

def greeting(hours, minutes):
  if -1 < hours < 25 and -1 < minutes < 61:
    if hours < 12:
      print("Good morning!")
    elif hours < 17:
      print("Good afternoon!")
    elif hours < 20:
      print("Good evening!")
    elif hours < 25:
      print("Good night!")
  else:
    print("Invalid!")\

greeting(hours, minutes)
