def greet(abc):
    def inner(*args, **kwargs):
        print(f"function : {abc.__name__}")
        abc(*args, **kwargs)
        print(f"Welcome to decorators!")
    return inner


# worked out decorators and multiple args and kwargs
@greet
def random_name(*args, **data):
    for i in args:
        print(f"Hi, {i}")
    
    for k, v in data.items():
        print(f"{k} is {v.upper()}")


random_name('Aashick', 'thahasin', 'shabbu', firstname='Aashick',
afirstname='Thahasin')