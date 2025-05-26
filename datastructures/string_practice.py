str = 'ABCDCDC'
substr = 'CDC'


def no_of_pattern(str,substr):
    start = 0
    cnt = 0
    while start < len(str):
        pos = str.find(substr)
        if pos != -1:
            cnt +=1
            start = pos+1
        else:
            print(f"{substr}Substring is not found")
    
print(no_of_pattern(str,substr))


start = 0
cnt = 0
while start < len(str):
    pos = str.find(substr)
    print(pos)