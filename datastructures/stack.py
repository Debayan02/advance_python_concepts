nested_json = {
    "name": "John",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "geo": {
            "lat": 40.7128,
            "lng": -74.0060
        }
    }
}

stack = [(nested_json, '|')]

flat_dict = {}
sep = "_"
while stack:
    print(stack)
    current, parent_key = stack.pop()
    print("-----Current key-----")
    print(current)
    print("------Parent Key-----------")
    print(parent_key)
    if isinstance(current,dict):
        for key,value in current.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            stack.append((value,new_key))
            print("---Here is the stack---")
            print(stack)
    elif isinstance(current,list):
        for index,value in enumerate(current):
            new_key = f"{parent_key}{sep}{index}"
            stack.append((value,new_key))
    else:
        flat_dict[parent_key]=current

print(flat_dict)