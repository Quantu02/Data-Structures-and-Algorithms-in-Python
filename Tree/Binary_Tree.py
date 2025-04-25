#%%
class Node:
    
    def __init__(self,key):
        self.value=key 
        self.left=None
        self.right=None 
        
#%%
class BinarySearchTree:
    
    def __init__(self):  
        self.root=None#empty ll
        self.n=0#no. of nodes
        
    #insert a node into the bst
    def insert(self,key):
        if self.root is None:
            self.root = Node(key)
            self.n+=1
            
        else:
            self.__insert_recursive(self.root,key)
            self.n+=1
            
    def __insert_recursive(self,node,key):
        if key<node.value:
            if node.left is None:
                node.left=Node(key)
            else:
                self.__insert_recursive(node,self.right,key)
        elif key> node.value:
            if node.right is None :
                node.right=Node(key)
            else:
                self.__insert_recursive(node.right,key)
    def size(self):
        return self.n
    
    def traverse(self):
        """Performs in-order traversal (left-root-right)"""
        result = []
        self.__inorder(self.root, result)
        return result

    def __inorder(self, node, result):
        if node:
            self.__inorder(node.left, result)
            result.append(node.value)
            self.__inorder(node.right, result)
     
    def search(self,key):
        return self._search_recursive(self.root,key)
        
    def _search_recursive(self,node,key):
        if node is None or node.value==key:
            return node
        if key<node.value:
            return self._search_recursive(node.left,key)
        return self._search_recursive(node.right,key)
     
     
    # Delete a node from the BST
    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key, it lies in the left subtree
        if key < root.value:
            root.left = self._delete_recursive(root.left, key)
        # If the key to be deleted is larger than the root's key, it lies in the right subtree
        elif key > root.value:
            root.right = self._delete_recursive(root.right, key)
        # If key is the same as root's key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.value = self._min_value_node(root.right).value

            # Delete the inorder successor
            root.right = self._delete_recursive(root.right, root.value)

        return root
            
    def display(self, node=None, level=0):
        """Displays the BST structure."""
        if node is None:
            node = self.root  # Start from root when called without arguments
        if node is not None:
            if node.right:
                self.display(node.right, level + 1)
            print(" " * (level * 4) + str(node.value))
            if node.left:
                self.display(node.left, level + 1)
                
# %%
node=Node(5)
# %%
print(node.right)
# %%
bst=BinarySearchTree()
# %%
bst.insert(5)
bst.insert(2)
bst.insert(6)
# %%
print(bst.root.value)
print(bst.root.right.value)
# %%
bst.traverse()
# %%
print(f'size of the tree is {bst.size()} ')
# %%
bst.search(5)
# %%
bst.display()