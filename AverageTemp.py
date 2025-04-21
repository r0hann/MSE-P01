import numpy as np
temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

# 2. Highest and lowest temperature recorded
highest_temp = np.max(temperatures)
lowest_temp = np.min(temperatures)
print(f"Highest temperature: {highest_temp}°C")
print(f"Lowest temperature: {lowest_temp}°C")
