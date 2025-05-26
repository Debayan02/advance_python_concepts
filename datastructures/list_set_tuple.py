"""foods = []
prices = []
total=0.00

while True:
    food = input("Enter the food you want(q to quit) :")
    if food.lower() == 'q':
        break
    else:
        foods.append(food)
        price = float(input("Enter the rpice of food :"))
        prices.append(price)

print("---------Your Cart-----------")
print(foods,end = " ")

print("----------Price of food--------------")
print(prices, end = " ")"""


#2D-Collections in python

"""questions = ("How many bones are there in human body?",
             "Which animal has the largest egg?",
             "What is the most abundant gas in atmosphere?",
             "Which planet in the solar system is the hottest",
             "How many elements are there in periodic table")

options = (("A.209","B.206","C.300","D.210"),
           ("A.Whale","B.Elephant","C.Ostrich","D.Mouse"),
           ("A.Nitrogen","B.Carbondioxide","Oxygen","Carbonmonoxide"),
           ("A.Mercury","B.Mars","C.Pluto","D.Earth"),
           ("A.118","B.116","C.119","D.120"))

answers = ("A","C","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your guess :")
    if guess == answers[question_num]:
        print("Correct Answer")
        score+=1
    else:
        print("Incorrect answer")
    question_num+=1"""


    #create a list of tuple which contains two nos from a list of integer nos so that the sum of pair is even

def even_sum_pair():
    nos = [3,4,5,6,7,8,9,10]
    result = []
    for i in range(len(nos)):
        for j in range(i+1,len(nos)):
            if ((nos[i]+nos[j]) % 2 == 0):
                result.append((nos[i],nos[j]))
    return result
    
print("--------Here is the pair of integers-----------")
print(even_sum_pair())