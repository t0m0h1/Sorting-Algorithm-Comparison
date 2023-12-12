# Within this script we will compare the performance of the different algorithms and visualise them

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import time
from bubblesort import bubblesort
from mergesort import mergesort

# Creating a random array of 1000 elements
array = np.random.randint(0, 10000, 10000)

# Creating a copy of the array
array1 = array.copy()
array2 = array.copy()

# Sorting the array using bubblesort
start = time.time()
bubblesort(array1)
end = time.time()

# Sorting the array using mergesort
start1 = time.time()
mergesort(array2)
end1 = time.time()

# Printing the time taken by each algorithm
print("Time taken by bubblesort algorithm:", end - start)
print("Time taken by mergesort algorithm:", end1 - start1)

# Plotting the graph
plt.plot(array1, label='bubblesort')
plt.plot(array2, label='mergesort')
plt.legend()
plt.title('Time Complexity of sorting algorithms')
plt.xlabel('Number of elements')
plt.ylabel('Time taken in milliseconds')
plt.show()

# Conclusion
# In this script we compared the performance of the bubblesort and mergesort algorithms.
# We found that the mergesort algorithm is faster than the bubblesort algorithm.
# The time complexity of the bubblesort algorithm is O(n^2) (linear) in worst case and O(n) in best case.
# The time complexity of the mergesort algorithm is O(nlogn) (logarithmic) in all cases.

