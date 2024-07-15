# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        tree = {}
        children_map = {}
        for i in descriptions:
            children_map[i[1]] = 1
            if tree.get(i[0]) is not None:
                if i[2]:
                    tree[i[0]][0] = i[1]
                else:
                     tree[i[0]][1] = i[1]
            else:
                if i[2]:
                    tree[i[0]] =  [i[1], 0]
                else:
                    tree[i[0]] = [0, i[1]]
        for i in list(tree.keys()):
            if children_map.get(i) is None:
                root_value = i
                break
    
        root_node = TreeNode(root_value,self.find_left_child(tree, root_value), self.find_right_child(tree, root_value))
        
        return root_node


    def find_right_child(self, tree, parent):
        if tree.get(parent) is not None:
            if tree[parent][1] != 0:
                right_value = tree[parent][1]
                node = TreeNode(right_value, self.find_left_child(tree, right_value), self.find_right_child(tree, right_value))
            else:
                node = None
        else:
            node = None

        return node
    

    def find_left_child(self, tree, parent):
        if tree.get(parent) is not None:
            if tree[parent][0] != 0:
                left_value = tree[parent][0]
                node = TreeNode(left_value, self.find_left_child(tree, left_value), self.find_right_child(tree, left_value))
            else:
                node = None
        else:
            node = None

        return node

        


        
