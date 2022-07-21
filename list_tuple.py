# lamda functions
x = lambda a : a + 10
print(x(5))

# multiple argument a, b and c return the result
z = lambda a, b, c : a + b + c
print(z(2, 3, 4))

# lambda with function
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(f"mytripler : {mytripler.__name__}")
print(mytripler(11))

# lambda with reduce