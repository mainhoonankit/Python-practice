#current age and future age
current_year = 2026
n = int(input("Enter your current age or birth year"))
if n<100:
 age = n
else:
 age = current_year - n
print("your current age is:", age)
print("your age after 10 years will be:", age +10)  