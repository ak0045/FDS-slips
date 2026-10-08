// Q1) A Write a Python program using Pandas to calculate the sum, average, median, mode, minimum, maximum, and standard deviation of the following marks: Marks = [72, 85, 91, 68, 85, 79, 94]

import pandas as pd
marks = pd.Series([72, 85, 91, 68, 85, 79, 94])
print(f"Sum: {marks.sum()}")
print(f"Average: {marks.mean():.2f}")
print(f"Median: {marks.median()}")
print(f"Mode: {marks.mode()[0]}")
print(f"Minimum: {marks.min()}")
print(f"Maximum: {marks.max()}")
print(f"Std Dev: {marks.std():.2f}")


// Q2) B Write a program to create two lists, one representing student names and the other representing percentage. Display the data in a pie chart and bar chart.

import matplotlib.pyplot as plt
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
percentages = [85, 92, 78, 65, 88]
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].pie(percentages, labels=names, autopct='%1.1f%%', startangle=90)
axes[0].set_title('Student Percentages (Pie Chart)')

axes[1].bar(names, percentages, color='skyblue')
axes[1].set_title('Student Percentages (Bar Chart)')
axes[1].set_ylabel('Percentage')

plt.tight_layout()
plt.show()


OR 
 
 
// Q2) B Write a program to create a DataFrame containing 2D coordinates of multiple data points. Write a Python program to select any two points and compute the Euclidean distance between them using 
numpy.linalg.norm(), showing both the difference vector and the final 
distance. 

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'X': [2, 5, 8, 12, 3],
    'Y': [3, 7, 1, 9, 10]
})

p1 = df.iloc[0].to_numpy()
p2 = df.iloc[1].to_numpy()

diff_vector = p2 - p1
distance = np.linalg.norm(diff_vector)

print(f"Point 1: {p1}")
print(f"Point 2: {p2}")
print(f"Difference Vector: {diff_vector}")
print(f"Euclidean Distance: {distance:.4f}")
