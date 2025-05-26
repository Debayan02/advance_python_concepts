"""name = input("Enter your name: ")
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

#print(f"Your name is {name}")"""


"""age = int(input("Enter your age: "))
while age < 0:
    print("Age can't be negative")
    age = int(input("Enter your age: "))
print(f"My age is {age}")"""


"""food = input("Enter a food you like (q to quit)")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (q to quit)")
print("Bye")"""

#print nos only between 1 and 10
"""num = int(input("Enter a number: "))
while  num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 an 10: "))
print(f"Your number is {num}")"""


"""n = 1
while not n >= 4:
    print("Pythoniesta")
    n+=1

n = 0
alist = []
while  n <= 4:
    alist.append(n)
    n+=1
print(alist)"""

"""time=0
rate=0
principal=0

while time <=0:
    if time <=0:
        time = int(input("Enter a time which is greater than 0 :"))
        print("Time can't be zero")
print(time)

while rate <= 0:
    if rate <=0:
        rate = int(input("Enter positive rate of interest :"))
        print("Rate of Interest can't be zero")


while principal <= 0:
    if principal <= 0:
        principal=int(input("Enter the principal amount :"))
        print("Principal can't be negative")

Amount = principal * pow((1+(rate/100)),time)
print(f"You final amount is : {Amount}")"""

principal=int(input("Enter the principal amount :"))
rate = int(input("Enter the rate of interest :"))
time = int(input("Enter the time :"))

while True:
    if principal < 0:
        print("Time can't be less than zero")
        time = int(input("Enter a positive principal :"))
    else:
        break

while True:
    if rate < 0:
        print("Rate can't be zero")
        Rate = int(input("Enter positive Rate of Interest :"))
    else:
        break

while True:
    if time < 0:
        print("Time can't be less than zero")
        time = int(input("Enter positive time :"))
    else:
        break

Amount = principal * pow((1+(rate/100)),time)
print(f"You final amount is : {Amount}")

