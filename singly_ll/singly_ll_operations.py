class Node:
    def __init__(self, val):
        self.data = val 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None

        def insert_beginning(self, val):
            '''
                Insert node at the beginning of the linked list.

                val type: int
                rtype: Node 

                Time: O(1)
                Space: O(n)

            '''
            new_node = Node(val)
            new_node.next = self.head 
            self.head = new_node 

            return self.head

        def insert_end(self, val):
            '''
                Insert node at the end of the linked list.

                val type: int
                rtype: Node 

                Time: O(n)
                Space: O(n)

            '''
            new_node = Node(val)

            if not self.head:
                self.head = new_node

            last = self.head 
            while(last.next): # Traverse and break at None 
                last = last.next
            last.next = new_node 

            return self.head

        def delete_node(self, position):
            '''
                Delete node at the given position.

                position type: int 
                rtype: Node

                Time: O(n)
                Space: O(n)

            '''
            dummy = self.head 
            if position == 0:
                return dummy.next
            
            while (position-1 > 0):
                dummy = dummy.next 
                position -= 1
            dummy.next = dummy.next.next 
            return dummy


        def find_node(self, val):
            '''
                
                Return True or False if a given value is present in the linked list. 

                val type: int
                rtype: bool

                Time: O(n)
                Space: O(n)
                

            '''
            dummy = self.head
            while (dummy.next != None):
                if dummy.data == val:
                    return True
                dummy = dummy.next  
            return False