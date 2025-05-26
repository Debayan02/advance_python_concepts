"""def fibonacci():
    count = 0
    n1,n2=0,1
    nterms=int(input("How many terms"))
    if nterms <=0:
        print("Please give some positive numbers")
    elif nterms==1:
        yield n1
    else:
        while count < nterms:
            if count == 0:
                count+=1
                yield n1
            elif count == 1:
                count+=1
                nth = n1+n2
                yield nth
            else:
                nth = n1+n2
                n1=n2
                n2=nth
                count+=1
                yield nth
            
for i in fibonacci():
    print(i, end =" ")"""




"""def fibonacci(nterms):
    count = 0
    n1,n2=0,1
    while count < nterms:
        if count == 0:
            count+=1
            yield n1
        elif count == 1:
            count+=1
            yield n2
        else:
            nth = n1+n2
            n1=n2
            n2=nth
            count+=1
            yield nth

for i in fibonacci(15):
    print(i, end = " ")"""


"""def fibonacci(nterms):
    n1,n2=0,1
    count = 1
    while count < nterms:
        if count == 1:
            nth = n1
            count+=1
            yield nth
        elif count == 2:
            nth = n1+n2
            count+=1
            yield nth
        else:
            n1 = n2
            n2 = nth
            nth = n1+n2
            count+=1
            yield nth

for i in fibonacci(10):
    print(i, end = " ")"""



"""def fibonacii(nterms):
    n1,n2 = 0,1
    count = 1
    while count < nterms:
        if count == 1:
            nth = n1
            count+=1
            yield nth
        elif count == 2:
            nth = n1+n2
            count+=1
            yield nth
        else:
            n1 = n2
            n2 = nth
            nth = n1+n2
            count += 1
            yield nth

for i in fibonacii(7):
    print (i, end = " ")"""



def fibonacci(nterms):
    n1,n2=0,1
    count = 1
    while count <= nterms:
        if count == 1:
            count +=1
            yield n1
        elif count == 2:
            count+=1
            yield n1+n2
        else:
            count+=1
            nth = n1+n2
            n1=n2
            n2=nth
            yield nth

for i in fibonacci(10):
    print(i, end = " ")