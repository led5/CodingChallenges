def uniquePathsWithObstacles(obstacleGrid):
        """
            Time: O(mn) where m and n is the size of the matrix
            Space: O(mn)
            
        """
        
        if obstacleGrid[0][0] == 1: 
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[0 for i in range(n)] for i in range(m)] 
        paths[0][0] = 1 # number of ways to reach first cell
        
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                paths[i][0] = 1
                
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                break
            else:
                paths[0][j] = 1 
        
        # Fill in remaining cells 
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                else:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[m-1][n-1]
            