class Node:
    def __init__(self, val):
        self.data = val  
        self.left = None
        self.right = None 

    def insert_node(self, root, val):
        '''
            Given a value, insert a new node into the tree. 

            root type: Node 
            val type: int
            rtype: Node 

        '''
        if not root: 
            return Node(val)
        else:
            if root.data == val:
                return root
            elif root.data < val:
                root.right = self.insert_node(root.right, val)
            else:
                root.left = self.insert_node(root.left, val)
        return root 
                
    def delete_node(self, root, val):
        '''
            Given a value, delete the node with the given value.

            root type: Node 
            val type: int
            rtype: None

        '''
        if not root:
            return None
        if val != root.data:
            if val < root.data:
                root = self.delete_node(root.left, val)
            elif val > root.data:
                root = self.delete_node(root.right, val)
            return root 
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            r_subtree = root.right
            while(r_subtree.left):
                r_subtree = r_subtree.left 
            r_subtree.left = root.left 
            return root.right
        return self.delete_node(root, val)

    def find_node(self,root, val):
        '''
            Find the given value of the BST. 
            
            root type: Node 
            val type: int
            rtype: None 

        '''
        while(root):
            if val < root.data:
                root = root.left
            elif val > root.data:
                root = root.data
            else:
                return root
        return None 

    def inorder_traversal(self, root):
        '''
            Print the BST inorder. 

            root type: Node 
            rtype: None
        '''
        if not root:
            return None
        print(root.left)
        print(root.data)
        print(root.right)

    def preorder_traversal(self, root):
        '''
            Print the BST preorder. 

            root type: Node 
            rtype: None 
        '''
        if not root:
            return None
        print(root.data)
        print(root.left)
        print(root.right)

    def postorder_traversal(self, root):
        '''
            Print the BST postorder. 

            root type: Node
            rtype: None
        '''
        if not root:
            return None
        print(root.left)
        print(root.right)
        print(root.data)

    def levelorder_traversal(self, root):
        '''
            Print the BST levelorder.

            root type: Node
            rtype: None 

        '''
        height = self.get_height(root)
        for i in range(1, height+1):
            self.print_levelorder(root, i)
        
    def get_height(self, root):
        if not root: 
            return 0
        return max(self.get_height(root.right), self.get_height(root.left)) + 1
    
    def print_levelorder(self, root, level):
        if not root:
            return None
        if level == 1:
            print(root.data)
        elif level > 1:
            self.print_levelorder(root.left, level-1)
            self.print_levelorder(root.right, level-1)



if __name__ == "__main__":

    root = Node(6)
    root = root.insert_node(root, 1)
    root = root.insert_node(root, 10)
    root = root.insert_node(root, 23)

    root = root.delete_node(root, 23)

    root = root.insert_node(root, 35)

    root = root.inorder_traversal(root)
    root = root.preorder_traversal(root)
    root = root.postorder_traversal(root)
    root = root.levelorder_traversal(root)


