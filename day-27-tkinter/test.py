def add(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum

print(add(1,2,3,4))

def calculate(num, **kwargs):
    # print(kwargs) # {'add': 3, 'multiply': 5}
    result = 0
    for key, value in kwargs.items():
        if key == "add":
            result += num + value
            break
        if key == "multiply":
            result += num * value
            break
    return result


print(calculate(5, add=3, multiply=5))