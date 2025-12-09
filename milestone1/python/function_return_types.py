from typeguard import typechecked  

@typechecked
def add(a:int,b:int)->int:
    return a+b

@typechecked
def greet(name:str)->str:
    return f"Hello, {name}"

@typechecked
def dict_print(data:list[str])->dict[str,int]:
    dict_data={}
    for index,value in enumerate(data):
        dict_data[value]=index
    return dict_data

print(add(1,2.8))
print(greet("Alice"))
print(dict_print(["apple","banana","cherry"]))

#run mypy "function_return_types.py" to check for static type errors
#run the code to check for dynamic type errors