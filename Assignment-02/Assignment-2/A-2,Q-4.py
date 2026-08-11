#Write a program to find the variance for the given
#dataset using logic and library function.
print("Using user logic:")
data=[10,12,15,18,20,20,22,25]
mean=sum(data)/len(data)
variance=0
for i in data:
    variance+=(i-mean)**2
variance=variance/len(data)
print("Variance:",variance)
print("Using inbuilt library:")
import numpy as np
data=[10,12,15,18,20,20,22,25]
print("Variance:",np.var(data))
