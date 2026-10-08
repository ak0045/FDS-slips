// Q1) A Create a DataFrame from a dictionary containing employee name, department, designation, and salary for at least 8 employees. Display only the first 5 records using a suitable Pandas function.

import pandas as pd
data = {
    'Employee_Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry'],
    'Department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'Marketing'],
    'Designation': ['Manager', 'Developer', 'Analyst', 'Developer', 'Executive', 'Manager', 'Lead', 'Executive'],
    'Salary': [60000, 75000, 50000, 70000, 45000, 80000, 90000, 48000]
}

df = pd.DataFrame(data)

print("First 5 Records:")
print(df.head(5))



Q2) B Write a program to create Dataset Name: StudentData.csv 
Save the following data in Excel and store it as a .CSV file. 

Name Address Age Class 
Smaran Pune 20 BE 
Sachin Mumbai 23 BSc(CS) 
Samarpan Delhi 19 BVoC 
Spandan Chennai 21 BCom 
Shravan Madurai 22 BSc 
 
  Import Dataset  
The dataset contains two categorical columns: 
• Name 
• Class 
Perform: 
a) One-Hot Encoding on Name column 
b) Label Encoding on Class column

import pandas as pd
from sklearn.preprocessing import LabelEncoder

raw_data = {
    'Name': ['Smaran', 'Sachin', 'Samarpan', 'Spandan', 'Shravan'],
    'Address': ['Pune', 'Mumbai', 'Delhi', 'Chennai', 'Madurai'],
    'Age': [20, 23, 19, 21, 22],
    'Class': ['BE', 'BSc(CS)', 'BVOC', 'BCom', 'BSc']
}
pd.DataFrame(raw_data).to_csv('StudentData.csv', index=False)

df = pd.read_csv('StudentData.csv')

df_encoded = pd.get_dummies(df, columns=['Name'])

le = LabelEncoder()
df_encoded['Class_Encoded'] = le.fit_transform(df['Class'])

print(df_encoded)



OR 
// Q2) B Write a program to generate a random array of 25 integers and display 
them using a line chart, scatter plot, histogram and box plot. Apply 
appropriate color, labels and styling options  

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
data = np.random.randint(1, 100, 25)

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot(data, color='blue', marker='o')
axes[0, 0].set_title('Line Chart')

axes[0, 1].scatter(range(len(data)), data, color='red')
axes[0, 1].set_title('Scatter Plot')

axes[1, 0].hist(data, bins=5, color='green', edgecolor='black')
axes[1, 0].set_title('Histogram')

axes[1, 1].boxplot(data, patch_artist=True)
axes[1, 1].set_title('Box Plot')

plt.tight_layout()
plt.show()

