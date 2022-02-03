'''
Merge Sort

-merge function that takes two sorted arrays and merges them into one
-merge sort function breaks an array down to its base case (single element) before recombining the fractions in order using merge.
-How & when to accomplish this?
    Create a lower half and an upper half to an array by breaking at midpoint
    Call merge_sort on each half, assigning result to a variable
    Call merge on the two halves
    Return the result

This appends to a new array each time merge is called. With a dynamic array this could be expensive.
There's an implementation using a buffer of length n that would be worth exploring as well.
'''

def merge(arr1, arr2):
    res = []
    i,j = 0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1
    res += arr1[i:]
    res += arr2[j:]
    return res

def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Break in half, recall recursively on each half, then recombine
    split_point = len(arr) // 2
    lower = merge_sort(arr[:split_point])
    upper = merge_sort(arr[split_point:])
    return merge(lower, upper)


if __name__ == "__main__":
    a = [-7,4,5,6,7,1,2,-7,10,4]
    print(merge_sort(a))