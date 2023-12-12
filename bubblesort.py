# The bubblesort algorithm is a simple sorting algorithm.
'''

It works by repeatedly stepping through the list to be sorted, comparing each pair of adjacent items 
and swapping them if they are in the wrong order.'''

def bubblesort(array):
    # Traverse through all array elements
    for i in range(len(array)):
        # last i elements are already in place
        for j in range(0, len(array))-i-1:
            # traverse the array from index 0 to n-i-1
            # swap if the element found is greater than the next element
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

# Driver code to test above
array = [64, 34, 25, 12, 22, 11, 90]
if __name__ == '__main__':
    bubblesort(array)
    print("Sorted array is:")
    for i in range(len(array)):
        print("%d" %array[i])
