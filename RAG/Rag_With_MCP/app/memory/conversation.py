conversion_memory=[]

def add_memory(role:str,content:str):
    conversion_memory.append({"role":role,"content":content})

def get_memory():
    return conversion_memory[:5]