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
    
    def is_prime(self):
      if self.number <= 1:
          return False  # Numbers less than or equal to 1 are not prime
      for i in range(2, int(self.number ** 0.5) + 1):
          if self.number % i == 0:
              return False  # Number is divisible by i, so it's not prime
      return True  # Number is prime if no divisors were found

    def display_result(self):
        print(f"The factorial of {self.number} is: {self.calculate()}")
        print(f"Is {self.number} a prime number? {'Yes' if self.is_prime() else 'No'}")
        

# Main code
if __name__ == "__main__":
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        factorial = FactorialCalculator(num)
        factorial.display_result()
    except ValueError:
        print("Please enter a valid integer.")
