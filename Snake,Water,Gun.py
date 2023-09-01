#snake,water,gun function
import random
print("write:\n5 for snake\n6 for water\n7 for gun")
List=[5,6,7]
computer=random.choice(List)
user=int(input("what do you choose snake,water,gun "))
print(f"your opponent move is {computer}")
#print(type(user))
if user==computer:
    print("it is draw")
elif user==computer-1:
    print("you won")
else:
    print("you lose")        