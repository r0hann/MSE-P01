#1- Activity : Create a NumPy array of the first 10 positive integers.

import numpy as np

# 1. Create the array
arr = np.random.randint(1, 101, size=10)

# 2. Print the array
print("Array:", arr)

# 3. Print shape and data type
print("Shape:", arr.shape)
print("Data type:", arr.dtype)

# 4. Multiply each element by 2
print("Multiplied by 2:", arr * 2)

#2- Activity : You are given the test scores of 5 students across 3 subjects in a 2D NumPy array. Each row represents a student, and each column a subject.

# Given scores
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# 1. Average score for each student (row-wise)
student_averages = np.mean(scores, axis=1)
print("Average score per student:", student_averages)

# 2. Average score for each subject (column-wise)
subject_averages = np.mean(scores, axis=0)
print("Average score per subject:", subject_averages)

# 3. Student with highest total score
total_scores = np.sum(scores, axis=1)
top_student_index = np.argmax(total_scores)
print("Top student index (highest total score):", top_student_index)

# 4. Add 5 bonus points to the third subject (column index 2)
scores[:, 2] += 5
print("Updated scores with bonus on third subject:\n", scores)
