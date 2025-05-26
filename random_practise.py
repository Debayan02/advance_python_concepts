str = "{[()]}"
stack = []
close_to_open = {'}':'{',']':'[',')':'('}
for s in str:
    if s in close_to_open.values():
        stack.append(s)
    elif s in close_to_open:
        if not stack:
            print("Invalid one")
        top = stack.pop()
        if top != close_to_open[s]:
            print("False")
if not stack:
    print("valid match")
else:
    print("Invalid match")


rdd = sc.textFile("words.txt")
counts = rdd.flatMap(lambda line: line.split(" ")).map(lambda word: (word,1)).reduceByKey(lambda x,y : x+y)