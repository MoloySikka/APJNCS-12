# Without function

start = int(input("Enter 'start' value: "))
stop = int(input("Enter 'stop' value: "))
step = int(input("Enter 'step' value: "))

range_list = []

i = 1

while i < stop:
  range_list.append(i)
  i += step

# With function
def my_range(start=0, stop=0, step=1):
  if start != 0 and stop == 0 and step == 1:
    stop = start
    start = 0

  range_list = []
  
  i = start
  while i < stop:
    range_list.append(i)
    i += step

  return range_list


print(my_range(start, stop, step))