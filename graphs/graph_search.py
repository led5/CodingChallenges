 from collections import deque
    
def bfs(graph, vertex):
    '''
        Queue implementation for bfs. 

        Time: O(V + E) wherte V is the number of vertices
        in the graph and E is the number of edges in the graph. 

        Space:  O(V), to visit each node. 

    '''
    q = deque()
    visited = [] 
    q.append(vertex)
    visited[vertex] = True 

    while (q):
        vertex = q.pop(0)
        
        for neighbor in graph[vertex]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True 

    
def dfs(graph, vertex):
    '''
        Stack implementation for DFS. 

        Time: O(V + E) where V is the number of vertices and E 
        is the number of edges 
        Space: O(V) for visited array

    '''

    visited = []
    stack = []
    stack.append(vertex)

    while(len(stack)):
        vertex = stack.top() 
        stack.pop()

        if (not visited[vertex]):
            visited[vertex] = True
        for node in adjacent[vertex]: 
            if (not visited[node]):
                stack.append(node)



