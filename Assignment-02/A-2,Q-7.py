#WAP to find the mean, median, mode, variance and standard deviation using inbuilt method by calling NumPy library.
import numpy as np
import statistics as stats

data = [10, 15, 20, 25, 30, 40, 45, 50, 55]

mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)
variance = np.var(data)
std = np.std(data)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std}")