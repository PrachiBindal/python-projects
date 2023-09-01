#exercise 2 from code with harry 
#print good morning ,afternoon,evening according to timestamp
import time
timestamp=time.strftime("%H:%M:%S")
hour=int(time.strftime("%H"))
#to great someone according to time
#time=int(input("tell me the time?\n"))
#print(type(hour))
if hour >= 3 and hour <12 :
    print("Good Morning")
elif hour >=12 and hour <17 :
    print("Good Afternoon")
elif hour >=17 and hour <22 :
    print("Good Evening")
else :
    print ("Good Night")                  