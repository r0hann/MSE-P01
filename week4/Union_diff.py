def unionOfStrings():
  farmyard_animals = {"goat", "dog", "pig"}
  household_pets = {"goldfish", "gerbil", "cat", "dog"}
  print(household_pets.union(farmyard_animals))

def unionOfnumbers():
  A = {10, 2, 3, 4}
  B = {39, 4, 5, 6}
  # Using '|' operator
  res1 = A | B
  print("using '|':", res1)
  
  # Using union() method
  res2 = A.union(B)
  print("using union():",res2)


def main():
  unionOfnumbers()

if __name__ == "__main__":
  main()