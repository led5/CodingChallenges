'''
Given the array A, print all the elements in reverse order.

'''

def reverse_list(A):
    if not A:
        print('List is empty...cannot reverse.')
    for i in range(len(A)-1, 0, -1):
        print(A[i])