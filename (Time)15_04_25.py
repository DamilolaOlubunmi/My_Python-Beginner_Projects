x = float(input("Please input time in minutes: "))
t_sec = x * 60
hours = int(t_sec//3600)
minutes = int((t_sec % 3600) // 60)
seconds = int(((t_sec % 3600) % 60)//60)
print("Hours: ", hours)
print("Minutes: ", minutes)
print("Seconds: ", seconds)
