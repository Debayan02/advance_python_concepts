menu={'popcorn':8.00,
      'soda':3.00,
      'pizza':10.00,
      'pretzel':5.00,
      'potato chips':6.00}


print("------------MENU----------------")
def show_menu():
    for key,value in menu.items():
        print(f'{key:10}:{value:.2f}')


print("------------YOUR CART------------")

def my_cart():
    cart=[]
    total=0
    while True:
        food = input(f"Select an item(q to quit)").lower()
        if food == 'q':
            break
        elif menu.get(food) is not None:
            cart.append(food)
        print(f"This is your order {cart}")
    if len(cart)>0:
        print("---Please check out your order----")
        order=input(f"Select an item(P to proceed)").lower()
        print("----------Your Itemized final bill---------")
        for i in cart:
            total+=menu.get(i)
            print(i,menu.get(i))
        print("-----------------Your Final Bill---------------")
        print(total)

show_menu()
my_cart()



n1,n2=0,1
count = 0
if nterms <= 0:
    print("Please make a positive number")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci series")
    while count < nterms:
        print(n1)
        nth = n1+n2
        n1=n2
        n2=nth
        count+=1