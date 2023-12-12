# The bubblesort algorithm is a simple sorting algorithm.
'''
It works by repeatedly stepping through the list to be sorted, comparing each pair of adjacent items 
and swapping them if they are in the wrong order.
'''

def bubblesort(array):
    n = len(array)
    # Traverse through all array elements
    for i in range(n):
        # last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from index 0 to n-i-1
            # swap if the element found is greater than the next element
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


# Driver code to test above
array = [64, 34, 25, 12, 22, 11, 90]
if __name__ == '__main__':
    print("Unsorted array is:")
    for i in range(len(array)):
        print("%d" %array[i])
    print("\n")
    bubblesort(array)
    print("Sorted array is:")
    for i in range(len(array)):
        print("%d" %array[i])


#the time complexity of the above algorithm is O(n^2) in worst case and O(n) in best case.
#the space complexity is O(1) as we are not using any extra space.

