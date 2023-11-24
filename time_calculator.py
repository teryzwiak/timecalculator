def add_time(start, duration, day=" "):

  dayinfo = ""
  
  timeStart, meridiem = start.split()
  hourStart, minuteStart = timeStart.split(":")
  
  hourDuration, minuteDuration = duration.split(":")

  #DEBUG1
  new_time = str(hourStart) + ":" + str(minuteStart) + " " + meridiem
  print(new_time)
  print("hourDuration:")
  print(hourDuration)
  print("minuteDuration:")
  print(minuteDuration)

  hourEnd = int(hourStart) + int(hourDuration)
  minutEnd = int(minuteStart) + int(minuteDuration)

  if(minutEnd>60):
    hourEnd += minutEnd//60
    minutEnd = minutEnd - 60

  if(hourEnd>12):
    hourEnd = hourEnd - 12
    meridiem = "PM"
  else:
    meridiem = "AM"

  print("f: ")
  
  if hourEnd>12 or meridiem=="PM":
    dayinfo = "(next day)"
    meridiem = "AM"
    f=hourEnd//24
    print(f)
    if(f>0):
      dayinfo = "(" + str(f) + " days later)"
      hourEnd = int(hourStart) + int(hourDuration) - (f * 24)
      print("houedn")
      print(hourEnd)
      if hourEnd>12 and meridiem=="PM":
        hourEnd = hourEnd - 12
        meridiem = "AM"
        f = f + 1
      if hourEnd>12 and meridiem=="AM":
        hourEnd = hourEnd - 12
        meridiem = "PM"
      dayinfo = "(" + str(f) + " days later)"
    

  if(minutEnd<10):
    minutEnd = "0" + str(minutEnd)
    
  #print(hourEnd)
  print("minutEnd")
  print(minutEnd)
  
  new_time = str(hourEnd) + ":" + str(minutEnd) + " " + meridiem + " " + dayinfo
  print("Exit time:")
  print(new_time)

  return new_time

add_time("3:00 AM", "60:10")
#add_time("11:43 AM", "00:20")
#add_time("10:10 PM", "3:30")
#add_time("11:30 AM", "20:32", "Monday")