import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hour=int(time.strftime('%H'))
print(hour)
minute=int(time.strftime('%M'))
print(minute)
second=int(time.strftime('%S'))
print(second)
if(hour>=5 and hour<12):
    print("GOOD MORNING")
elif(hour>=12 and hour <17):
    print("GOOD AFTERNOON")
elif(hour>=17 and hour<21):
    print("GOOD EVENING")
else:
    print("GOOD NIGHT")            
