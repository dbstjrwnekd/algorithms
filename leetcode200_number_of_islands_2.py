class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        check = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        answer = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if not check[x][y] and grid[x][y] == '1':
                    self.dfs((x,y), grid, check)
                    answer += 1
        
        return answer
    
    def dfs(self, current, grid, check):
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]
        
        cur_x, cur_y = current
        check[cur_x][cur_y] = True
        
        for i in range(4):
            next_x, next_y = cur_x + dx[i], cur_y + dy[i]
            
            if 0 <= next_x < len(grid) and 0 <= next_y < len(grid[0]):
                if not check[next_x][next_y] and grid[next_x][next_y] != '0':
                    self.dfs((next_x, next_y), grid, check)
