"""def my_decorator(func):
    def wrapper():
        func()
        print("Here are some sprinkles added to your icecream")
    return wrapper

def my_decorator2(func):
    def inner():
        func()
        print("Here is your fudge")
    return inner

    
@my_decorator2    
@my_decorator
def  get_icecream():
    print("Here is your ice-cream")
    
get_icecream()"""

###Decorator to log the arguments of the function####

def decorator(func):
    def wrapper(*args):
        print(f"Calling the {func.__name__} with args: {args}")
        result = func(*args)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@decorator
def multiply(x, y):
    return x*y

result = multiply(10,20)
print("Result: ", result)