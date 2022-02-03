'''
High level:
-In-place sorting algorithm
-Select a pivot from the array, then partition the other elements according to whether they are greater or less than the pivot.
-Sort the subarrays with a recursive call

Details:
-Each recursive call use two pointers starting at the beginning and end of the array section
-Goal is to move numbers bigger than pivot to the right side and those smaller to the left
-Do this by using two pointers. If the value at the small pointer is > pivot and value at the big pointer is < pivot then swap them.
-Where they meet is the position that the pivot can be swapped to. Then everything left of it is <= and everything right is >.
'''


def quicksort(nums, start_idx, end_idx):
    # Base case: we have 1 or fewer elements to consider so we're done
    if start_idx >= end_idx:
        return

    # Choose the first element as the pivot
    piv = nums[start_idx]
    s,e = start_idx, end_idx

    while s < e:
        # If this number is > pivot then it's fine where it is. Decrement e
        if nums[e] > piv:
            e -= 1
        # If this number is <= pivot then it's fine where it is so increment up
        elif nums[s] <= piv:
            s += 1
        # Otherwise these are in the wrong positions. Swap them
        else:
            nums[s], nums[e] = nums[e], nums[s]

    # Done rearranging. Use the final pointer indices to swap the pivot into its correct spot and make a recursive call with the two halves
    # After this, s == e and will be in the position that pivot can be swapped into.
    # Then everything left of this idx is <= pivot and everything right is greater
    nums[start_idx], nums[s] = nums[s], nums[start_idx]

    quicksort(nums, start_idx, s-1)
    quicksort(nums, s+1, end_idx)

    
if __name__ == "__main__":
    arr = [6,1,7,9,3,8,2,5,4,0]
    quicksort(arr, 0, len(arr)-1)
    print(arr)