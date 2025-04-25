def factorialOfValue(x):
    fact = 1
    print("x", x)
    for i in range(1, x+1):
        fact = fact * i
    return fact
factValue = factorialOfValue(4)
print("Factorial value of 4 is ", factValue)