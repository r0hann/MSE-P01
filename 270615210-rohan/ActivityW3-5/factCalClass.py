class FactorialCalculator:
    def __init__(self, number):
        self.number = number

    def calculate(self):
        if self.number == 0 or self.number == 1:
            return 1
        else:
            result = 1
            for i in range(1, self.number + 1):
                result *= i
            return result

    def display_result(self):
        print(f"The factorial of {self.number} is: {self.calculate()}")

# Main code
if __name__ == "__main__":
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        factorial = FactorialCalculator(num)
        factorial.display_result()
    except ValueError:
        print("Please enter a valid integer.")
