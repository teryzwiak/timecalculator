def add_time(start, duration, *day):
  #initialization of dayInfo
  dayInfo = ""
  nextDay = 0 
  f = 0

  #Start time divided to hourStart, minuteStart, meridiem
  timeStart, meridiem = start.split()
  hourStart, minuteStart = timeStart.split(":")
  
  #Duration time divided to hourDuration, minuteDuraton
  hourDuration, minuteDuration = duration.split(":")
  meridiem = str(meridiem)
  #DEBUG1
  current_time = str(hourStart) + ":" + str(minuteStart) + " " + meridiem
  print("current time:")
  print(current_time)
  print("hourDuration:")
  print(hourDuration)
  print("minuteDuration:")
  print(minuteDuration)
  print(day)

  hourDuration = int(hourDuration) 
  minuteDuration = int(minuteDuration)

  if(minuteDuration>60):
    hourDuration += minuteDuration//60
    minuteDuration = minuteDuration - (60 * (minuteDuration//60))

  hourEnd = int(hourStart) + hourDuration
  minutEnd = int(minuteStart) + minuteDuration
  
  if(minutEnd >= 60):
    hourEnd = hourEnd + 1
    minutEnd = minutEnd - (60 * (minutEnd//60))
 
  if(hourEnd > 24):
   f = hourEnd // 24
   hourEnd = hourEnd - (f * 24) 
   nextDay = f

  if(hourEnd == 12):
    if(meridiem == "AM"):
      print("działa")
      if(hourEnd != 12): hourEnd = hourEnd - 12
      meridiem = 'PM'
      print(meridiem)
    elif(meridiem == 'PM'):
      meridiem = 'AM'
      #hourEnd = hourEnd - 12
      print("działa2")
      nextDay += 1
  elif(hourEnd > 12):
    if(meridiem == 'AM'):
        if(hourEnd != 12): hourEnd = hourEnd - 12
        meridiem = 'PM'
    elif(meridiem == 'PM'):
        meridiem = 'AM'
        if(hourEnd != 12): hourEnd = hourEnd - 12
        nextDay += 1
    

  print("f: ")
  print(f)
  
  if(nextDay == 1):
    dayInfo = "Next day"
  else:
    dayInfo = str(nextDay) + " days later"


  if(minutEnd<10):
    minutEnd = "0" + str(minutEnd)
    
  new_time = str(hourEnd) + ":" + str(minutEnd) + " " + meridiem + " " + str(dayInfo)
  print("Exit time:")
  print(new_time)

  print("=====================================================")
  return new_time


add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)