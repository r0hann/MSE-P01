# MSE-P01
## Activity 1: NumPy Array of First 10 Positive Integers

### Objective:
- Create a NumPy array containing the first 10 positive integers.
- Perform basic operations to understand shape, data type, and element-wise computation.

### Steps:
1. Create a NumPy array with random values from 1 to 101.
2. Print the array.
3. Print the shape and data type of the array.
4. Multiply each element by 2 and print the result.

### Output Example:
```python
Array: [ 1  2  3  4  5  6  7  8  9 10]
Shape: (10,)
Data type: int64
Multiplied by 2: [ 2  4  6  8 10 12 14 16 18 20]
```

---

## Activity 2: Student Score Analysis Using 2D NumPy Arrays

### Objective:
Analyze the scores of 5 students across 3 subjects using NumPy.

### Given:
A 2D NumPy array where:
- Rows represent students
- Columns represent subjects

```python
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])
```

### Tasks:
1. Calculate and print the **average score for each student**.
2. Calculate and print the **average score for each subject**.
3. Identify and print the **student index with the highest total score**.
4. Add **5 bonus points** to the **third subject** for all students.

### Sample Output:
```python
Average score per student: [84.33, 86.33, 82.67, 92.33, 75.0]
Average score per subject: [83.0, 82.6, 86.8]
Top student index (highest total score): 3
Updated scores with bonus on third subject:
[[ 78  85  95]
 [ 88  79  97]
 [ 84  76  93]
 [ 90  93  99]
 [ 75  80  75]]
```
