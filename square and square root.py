import math
choice = input("enter your choice \n square \n square root ")
num = int(input("enter a number"))
if choice == "square":
    print("square of the number is:",num*num)
elif choice == "square root":
    print("square root of the number is:", math.sqrt(num)) 
else:
    print("invalid choice")      