# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        nums_list=[]
        nums_list=self.ss(root,nums_list)
        return ''.join(nums_list)

    def ss(self,tree,nums_list):
        if tree is None:
            nums_list.append('s')
            return nums_list
        val=tree.val
        nums_list.append(val)
        self.ss(tree.left,nums_list)
        self.ss(tree.right, nums_list)



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data_li=list(data)
        new_li=[]
        for i in data_li:
            if i=='s':
                new_li.append(TreeNode())
            else:
                new_li.append(TreeNode(i))


        while new_li:
            start_nodee.val=data_li.pop(0)







# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))