# the merge sort algorithm is a divide and conquer algorithm.
# it works by dividing the array into two halves, 
# calling itself for the two halves and then merging the two sorted halves.



def mergesort(arr):
    if len(arr) > 1:
        # finding the middle of the array
        mid = len(arr)//2
        # dividing the array elements into 2 halves (left and right)
        L = arr[:mid]
        R = arr[mid:]
        # sorting the first half
        mergesort(L)
        # sorting the second half
        mergesort(R)
        i = j = k = 0
        # copy data to temp arrays L[] and R[]




array = [64, 34, 25, 12, 22, 11, 90]

if __name__ == '__main__':
    print('\n')
    print("Merge Sort", '\n')
    print("Unsorted array is:")
    for i in range(len(array)):
        print("%d" %array[i])
    print("\n")
    mergesort(array)
    print("Sorted array is:")
    for i in range(len(array)):
        print("%d" %array[i])