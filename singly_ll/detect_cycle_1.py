'''
    Return True or False if a given 
    singly linked list contains a cycle.

    head type: Node 
    rtype: bool 
    
    Time: O(n) where n is the number of nodes
    Space: O(1)
'''

def has_cycle(head):
    if not head:
        return False 
    dummy = head.next 
    while(head != dummy):
        if (not head or not dummy):
            return False 
        head = head.next 
        dummy = dummy.next.next 
    return True 