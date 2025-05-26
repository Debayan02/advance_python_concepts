
"""def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b=b,a
        print("Here is the result")
        func(a,b)
    return inner

@smart_div
def div(a,b):
    print(a/b)
print(div(24,12))"""

"""def main():
    div(24,12)


if __name__== '__main__':
    main()"""


def log_cube(func):
    def wrapper(num):
        if num > 5:
            return num ** 3
        else:
            return num ** 2
    return wrapper

@log_cube
def find_square(num):
    return num ** 2

print(find_square(6))

"""import time
def log_func_time(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(args)
        end_time = time.time()
        exec_time = end_time - start_time
        print(f"Function {func.__name__} took {exec_time}ms")
    return wrapper


@log_func_time    
def calculate_multiply(nums):
    tot = 1
    for num in nums:
        tot*=1
    return tot

calculate_multiply([1,2,3,4,5])"""

def chng_type(func):
    def wrapper(nos):
        print("The resulttant datatype is :")
        x=func(nos)
        return x
    return wrapper

@chng_type
def sum_func(nums):
    tot = 0
    for num in nums:
        tot+= num
    return tot

print(sum_func([1,2,3,4]))
