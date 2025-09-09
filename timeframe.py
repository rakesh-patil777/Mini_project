import time
name=input("Enter ur name: ")
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hour=int(time.strftime('%H'))
if (hour>=0 and hour<12):
    print("Good Morning ", name)
if (hour>=12 and hour<17):
    print("Good Afternoon ", name)
if (hour>17 and hour<0):
    print("Good Evening ", name)  

