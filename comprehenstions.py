# from decorator_examp import random_name
# dictionary comprehension

# dict1 = dict([[i, i*10] for i in range(5)])

# print(dict1)
# print(type(dict1))

# # list comprehension

# lis1 = [i for i in range(1, 5) if i%2 == 0]
# print(lis1)

# # tuple comprehension
# tup1 = [i for i in range(1, 5) if i%2 == 0]
# print(tup1)


# generators in python
def table(n):  
    for i in range(n):  
        yield i

for i in table(15):
    print(i)