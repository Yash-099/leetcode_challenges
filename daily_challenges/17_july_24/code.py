# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest = self.return_the_forest(root, to_delete, False)
        return forest


    def return_the_forest(self, node, to_delete, has_parent, parent=None, is_right_child=False): # send parent node only if has_parent is true
        if node.val in to_delete:
            to_delete.remove(node.val)
            # removing from the parent node
            if has_parent:
                if is_right_child:
                    parent.right = None
                else:
                    parent.left = None
            if node.left is None and node.right is None:
                return []
            elif node.left is None:
                return self.return_the_forest(node.right, to_delete, False)
            elif node.right is None:
                return self.return_the_forest(node.left, to_delete, False)
            else:
                return self.return_the_forest(node.left, to_delete, False) + self.return_the_forest(node.right, to_delete, False)

        else:
            if node.left is None and node.right is None:
                if not has_parent:
                    return [node]
                else:
                    return []

            elif node.left is None:
                if not has_parent:
                    return [node] + self.return_the_forest(node.right, to_delete, True, node, True)
                else:
                    return self.return_the_forest(node.right, to_delete, True, node, True)

            elif node.right is None:
                if not has_parent:
                    return [node] + self.return_the_forest(node.left, to_delete, True, node, False)
                else:
                    return self.return_the_forest(node.left, to_delete, True, node, False)
            
            else:
                if not has_parent:
                    return [node] + self.return_the_forest(node.left, to_delete, True, node, False) + self.return_the_forest(node.right, to_delete, True, node, True)
                else:
                    return self.return_the_forest(node.left, to_delete, True, node, False) + self.return_the_forest(node.right, to_delete, True, node, True)
