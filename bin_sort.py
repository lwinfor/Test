from http import server
import os

class Node:
    def __init__(self,val=0):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self,arr) -> None:
        if len(arr) < 1:
            return
        self.root = Node(arr[0])
        for item in arr[1:]:
            self.insert(self.root,item)
        
    def insert(self,root,data):
        cur = self.search(root,data)
        node = Node(data)
        if data > cur.val:
            cur.right = node
        else:
            cur.left = node
        return 

    def search(self,root,data):
        cur = root
        while not cur is None:
            ans = cur
            if data > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        return ans

    def Pprint(self):
        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            print(node.val)
            dfs(node.right)
        dfs(self.root)

if __name__ == "__main__":
    arr = [2,3,4,5,1,3,9,3]
    bst = BST(arr)
    bst.Pprint()