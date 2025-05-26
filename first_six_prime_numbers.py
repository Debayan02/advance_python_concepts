"""def prime_series():
    count = 0
    while count <= 6:
        for n in range(2,100):
            for i in range(2,n-1):
                if count <=6:
                    if n%i != 0:
                        yield n
                        count+=1
                else:
                    break

for i in prime_series():
    print(i, end = " ")"""

def prime_series():
    prime = set()
    kterms = int(input("How many terms series ? "))
    for n in range(2,kterms):
        if n == 2:
            prime.add(n)
        else:
            for i in range(2,n):
                if n!=i and n%2 !=0:
                    prime.add(n)
    return prime

print(prime_series())



