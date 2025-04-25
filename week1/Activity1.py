import numpy as np

# Create a NumPy array of the first 10 positive integers
arr = np.random.randint(1, 101, size=10)

# Print the array
print("Original array:", arr)

# Print the shape and data type of the array
print("Shape of array:", arr.shape)
print("Data type of array:", arr.dtype)

# Multiply each element by 2 and print the result
doubled = arr * 2
print("Array multiplied by 2:", doubled)
