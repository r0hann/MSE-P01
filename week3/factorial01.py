def factorialOfValue(x):
    fact = 1
    if x < 0:
        return 1
    for i in range(1, x+1):
        fact *= i
    return fact
value = int(input("Enter the value for factorial: "))
factValue = factorialOfValue(value)
print("Factorial value is ", factValue)