# Aggregate and summarize the data
import pandas as pd

# Create a DataFrame with your data
df = pd.DataFrame({'id': ['E02007', 'E02007', 'E02008', 'E02008', 'E02008', 'E02009'],
                   'age': [10, 15, 5, 8, 12, 20]})

# Aggregate data by category and calculate sum
aggregated_data = df.groupby('id').sum()

# Summarize data by category
summary_data = df.groupby('id').agg({'age': ['count', 'mean', 'min', 'max']})

print(aggregated_data)
print(summary_data)


"""
# Create a list of 1000 random integers between 1 and 100000, then calculate the Z-Score to check for the outliers. Consider values Z-Score > 2 as outliers
import random
import statistics

# Generate a list of 1000 random integers between 1 and 100000
random_numbers = [random.randint(1, 100000) for _ in range(1000)]

# Calculate the mean and standard deviation
mean = statistics.mean(random_numbers)
std_dev = statistics.stdev(random_numbers)

# Calculate the Z-Scores for each number
z_scores = [(num - mean) / std_dev for num in random_numbers]

# Identify outliers with Z-Score > 2
outliers = [num for num, z_score in zip(random_numbers, z_scores) if abs(z_score) > 2]

# Print the outliers
print("Outliers:",outliers)

"""
"""
# Create a list of 100 random pair of integers (x,y) between 1 and 100. Draw visualization of the data using different - (10 pt) Draw scatter plot of the numbers using Python

import random
import matplotlib.pyplot as plt


p= [(random.randint(1, 100), random.randint(1, 100)) for _ in range(100)]

x = [pair[0] for pair in p]
y= [pair[1] for pair in p]

plt.scatter(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random Pairs of Integers')
plt.show()

"""
"""

# Create a list of 10 random integers between 1 and 100. - Standardize the numbers - Normalize the numbers • (10 pt) Solve the exercise using Python • (10 pt) Comment on the results you find
import random
import statistics


random_numbers = [random.randint(1, 100) for _ in range(10)]


mean = statistics.mean(random_numbers)
std_dev = statistics.stdev(random_numbers)
standardized_numbers = [(num - mean) / std_dev for num in random_numbers]


min_value = min(random_numbers)
max_value = max(random_numbers)
normalized_numbers = [(num - min_value) / (max_value - min_value) for num in random_numbers]


print("Original Numbers:")
print(random_numbers)
print("Standardised Numbers:")
print(standardized_numbers)
print("Normalised Numbers:")
print(normalized_numbers)
"""
"""
import random
import statistics

random_integers = [random.randint(1, 100000) for _ in range(1000)]
mean = statistics.mean(random_integers)
std_dev = statistics.stdev(random_integers)
z_scores = [(x - mean) / std_dev for x in random_integers]

outliers = [x for x in random_integers if abs((x - mean) / std_dev) > 2]

print("Number of outliers:", len(outliers))
print("Outliers:", outliers)
"""