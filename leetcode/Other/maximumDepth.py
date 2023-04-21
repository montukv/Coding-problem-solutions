
'''104. Maximum Depth of Binary Tree
Easy

2256

69

Add to List

Share
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.'''


class node:
    def __init__ (self,data = None):
        self.data=data
        self.left = None
        self.right = None

class tree:
    def __init__ (self):
        self.root = None

    def insert(self , value) :
        if self.root == None:
            self.root = node(value)
        else : 
            self._insert(value , self.root)

    def _insert(self, value ,cur_node):
        if value < cur_node.data :
            if cur_node.left == None:
                cur_node.left = node(value)
            else : 
                self._insert(value , cur_node.left)

        elif value > cur_node.data:
            if cur_node.right == None:
                cur_node.right = node(value)
            else : 
                self._insert(value,cur_node.right)

        else :
            print("Value is already in the tree ")
            
    def depth(self):
        if self.root != None: 
            return self._depth(self.root , 0)
        else : 
            return 0

    def _depth(self , cur_node , cur_depth): 
        if cur_node == None : 
            return cur_depth
        else  :
            left_depth = self._depth(cur_node.left , cur_depth + 1 )
            right_depth = self._depth(cur_node.right , cur_depth + 1)
            return max(left_depth , right_depth)



t = tree()
for _ in range(int(input("\nEnter the number of nodes : "))):
    t.insert(int(input()))
print("Depth : ",t.depth())

