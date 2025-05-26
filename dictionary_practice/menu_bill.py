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
    while True:
        food = input(f"Select an item(q to quit)").lower()
        if food == 'q':
            break
        elif menu.get(food) is not None:
            cart.append(food)
        print(f"This is your order {cart}")

show_menu()
my_cart()




