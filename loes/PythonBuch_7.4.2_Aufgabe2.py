# Gegeben ist folgendes Programm:
def f2(d):
    return 2**d

def f3(d):
    return 3**d

def f5(d):
    return 5**d

def f7(d):
    return 7**d

def add_function(f,g):
    return f(2) + g(2)

print(add_function(f2, f3))
print(add_function(f5, f7))


###################### lambda-Variante ######################

def add_function2(f, g):
    return f(2) + g(2)

inner_lambda = lambda x,d : x**d
# Idee: outer_lambda = lambda d : inner_lambda(2,d)

print(add_function2(lambda d: inner_lambda(2,d), lambda d: inner_lambda(3,d)))
print(add_function2(lambda d: inner_lambda(5,d), lambda d: inner_lambda(7,d)))


