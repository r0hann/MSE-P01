import numpy as np

# Temperature data in Celsius
temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

# 1. Average temperature for the week
average_temp = np.mean(temperatures)
print(f"Average temperature: {average_temp:.2f}°C")

# 2. Highest and lowest temperature recorded
highest_temp = np.max(temperatures)
lowest_temp = np.min(temperatures)
print(f"Highest temperature: {highest_temp}°C")
print(f"Lowest temperature: {lowest_temp}°C")

# 3. Convert all temperatures to Fahrenheit
temperatures_f = temperatures * 9 / 5 + 32
print("Temperatures in Fahrenheit:", temperatures_f)

# 4. Identify the days (by index) where the temperature was above 20°C
above_20_indices = np.where(temperatures > 20)[0]
print("Days with temperature above 20°C (by index):", above_20_indices)
