'''
    Return True or False if a given 
    singly linked list contains a cycle.

    head type: Node 
    rtype: bool 
    
    Time: O(n) where n is the number of nodes
    Space: O(n)

'''
def has_cycle(head):
    seen = set()
    while head:
        if head in seen:
            return True 
        seen.add(head) 
        head = head.next 
    return False 