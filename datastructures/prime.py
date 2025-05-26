def prime_number(num):
    for i in range(2,num-1):
        if num % i == 0:
            break
        else:
            return num
print(prime_number(14))