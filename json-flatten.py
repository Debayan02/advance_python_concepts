nested_json = {
    "name": "John",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "geo": {
            "lat": 40.7128,
            "lng": -74.0060
        },
    "salary" : [20,30,40]
    }
}
#rint(nested_json.get("address").get("street"))

"""def flatten_json(nested_json):
    flattened_dict = {}
    for key,value in nested_json.items():
        if isinstance(value, dict):
            flattened_dict.update(flatten_json(value))
        else:
            flattened_dict[key]=value
                              
    return flattened_dict

print(flatten_json(nested_json))"""






def flatten_json(nested_json,parent_key,sep=','):
    flattened_dict = {}
    for key,value in nested_json.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value,dict):
            flattened_dict.update(flatten_json(value,new_key,sep))
        elif isinstance(value,list):
            for i,item in enumerate(value):
                #flattened_dict.update(f"{new_key}[{i}]":f{"item"})
                flattened_dict[f"{new_key}[{i}]"]=item
        else:
            flattened_dict[key]=value
    return flattened_dict

#print(flatten_json(nested_json,"","."),end= ' ')






"""def flatten_json(nested_json,parent_key,sep='.'):
    flattend_dict = {}
    for key,value in nested_json.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value,dict):
            flattend_dict.update(flatten_json(value,new_key,sep))
        elif isinstance(value,list):
            for i,items in enumerate(value):
                flattend_dict[f"{new_key}{[i]}"]=items
        else:
            flattend_dict[key]=value
    return flattend_dict"""




"""def flatten_json(nested_json,parent_key,sep='.'):
    flattened_dict = {}
    for key,value in nested_json.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened_dict.update(flatten_json(value,new_key,sep))
        elif isinstance(value, list):
            for i,items in enumerate(value):
                if isinstance(value, dict):
                    flattened_dict.update(flatten_json(items,f"{new_key}[{i}]",sep))
                else:
                    flattened_dict[f"{new_key}[{i}]"] = items
        else:
            flattened_dict[key] = value
    return flattened_dict

print(flatten_json(nested_json2,"","."))"""





"""nums = [1,2,[4,6],[7,8],[45,[6,7,8]]]

def addition(nums):
    sum = 0
    for items in nums:
        if isinstance(items,list):
            sum+=addition(items)
        else:
            sum+=items
    return sum

print(addition(nums))"""


def flatten_json(nested_json,parent_key,sep="."):
    flattend_dict = {}
    for key,value in nested_json.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value,dict):
            flattend_dict.update(flatten_json(value,new_key,sep='.'))
        elif isinstance(value,list):
            for i,item in enumerate(value):
                if isinstance(item,dict):
                    flattend_dict.update(flatten_json(item,f"{new_key}[{i}]",sep='.'))
                else:
                    flattend_dict[f"{new_key}[{i}]"] = item
        else:
            flattend_dict[key] = value
    return flattend_dict

print(flatten_json(nested_json,"","."))








