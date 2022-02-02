# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ArrayToTree:
    '''
    Given a sorted (ascending) array build a height balanced BST (meaning sub-tree depths never differ by more than 1)
    Strategy: middle element of array is the current Node value. All smaller elements are in the left child, all larger
    are in the right child.
    Build tree recursively.
    '''
    def sorted_array_to_BST(self, nums):
        if len(nums) == 0:
            return None
        
        mid = len(nums)//2
        
        return TreeNode(val=nums[mid],
                left=self.sorted_array_to_BST(nums[:mid]),
                right=self.sorted_array_to_BST(nums[mid+1:]))