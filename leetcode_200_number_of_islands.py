class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        answer = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.dfs((i,j), grid)
                    answer += 1
                    
        return answer
    
    def dfs(self, start, grid):
        stack = [start]
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while stack:
            cur_x, cur_y = stack.pop()
            for i in range(4):
                next_x, next_y = cur_x + d[i][0], cur_y + d[i][1]
                if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
                    if grid[next_x][next_y] == '1':
                        grid[next_x][next_y] = '0'
                        stack.append((next_x,next_y))
        