# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeTraversal:
    # Recursive call: left subtree before right
    def pre_order(self, root):
        if root is None:
            return []
        return [root.val] + self.pre_order(root.left) + self.pre_order(root.right)

    def in_order(self, root):
        if root is None:
            return []
        return self.in_order(root.left) + [root.val] + self.in_order(root.right)

    def post_order(self, root):
        if root is None:
            return []
        return self.post_order(root.left) + self.post_order(root.right) + [root.val]

    def level_order(self, root):
        nodes = [root]
        order = []
        while len(nodes) > 0:
            node = nodes.pop(0)
            order.append(node.val)
            if node.left: nodes.append(node.left)
            if node.right: nodes.append(node.right)
        return order



if __name__ == "__main__":
    t7 = TreeNode(3)
    t6 = TreeNode(12, left=t7)
    t5 = TreeNode(10, right=t6)
    t4 = TreeNode(7)
    t3 = TreeNode(1)
    t2 = TreeNode(5, left=t3, right=t4)
    t1 = TreeNode(8, left=t2, right=t5)

    trav = TreeTraversal()
    # Preorder: 8,5,1,7,10,12,3
    print(trav.pre_order(t1))

    # Inorder: 1,5,7,8,10,3,12
    print(trav.in_order(t1))

    # Postorder: 1,7,5,3,12,10,8
    print(trav.post_order(t1))

    # Levelorder: 8,5,10,1,7,12,3
    print(trav.level_order(t1))