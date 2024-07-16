# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # start_node_path = self.path_from_node(root, startValue)
        # end_node_path = self.path_from_node(root, destValue)
        _, start_node_path = self.is_value_under_node(root, startValue, '')
        _, end_node_path = self.is_value_under_node(root, destValue, '')

        print(start_node_path, end_node_path, '\n')
        common_path_len = 0

        min_length = min(len(start_node_path), len(end_node_path))
        for i in range(min_length):
            if start_node_path[i] == end_node_path[i]:
                common_path_len += 1
            else:
                break

        start_node_path = start_node_path[common_path_len:]
        end_node_path = end_node_path[common_path_len:]

        print(start_node_path, end_node_path)
        path = 'U'*len(start_node_path) + end_node_path

        return path

    def path_from_node(self, node: TreeNode, val: int) -> str:
        if node.val == val:
            return ''
        elif (node.left is not None) and self.is_value_under_node(node.left, val):
            return 'L' + self.path_from_node(node.left, val)
        else:
            return 'R' + self.path_from_node(node.right, val)
        
    # def is_value_under_node(self, node: TreeNode, val:int) -> bool:
    #     if node.val == val:
    #         return True
    #     elif node.left is None and node.right is None:
    #         return False, None
    #     elif node.left is None:
    #         return self.is_value_under_node(node.right, val), 
    #     elif node.right is None:
    #         return self.is_value_under_node(node.left, val)
    #     else:
    #         return self.is_value_under_node(node.left, val) or self.is_value_under_node(node.right, val)

    def is_value_under_node(self, node: TreeNode, val:int, path_till_now: str) -> bool:
        if node.val == val:
            return True, path_till_now
        elif node.left is None and node.right is None:
            return False, ''
        elif node.left is None:
            present, path = self.is_value_under_node(node.right, val, path_till_now)
            if present:
                return True, 'R' + path
            else:
                return False, ''
        elif node.right is None:
            present, path = self.is_value_under_node(node.left, val, path_till_now)
            if present:
                return True, 'L' + path
            else:
                return False, ''
        else:
            present_left, path_left = self.is_value_under_node(node.left, val, path_till_now)
            present_right, path_right = self.is_value_under_node(node.right, val, path_till_now)
            if present_left:
                return True, 'L' + path_left
            elif present_right:
                return True, 'R' + path_right
            else:
                return False, 'None'
