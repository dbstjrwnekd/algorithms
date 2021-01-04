class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m, self.n = len(grid), len(grid[0])
        self.dx, self.dy = [0,0,-1,1], [1,-1,0,0]
        
        answer = 0
        for x in range(self.m):
            for y in range(self.n):
                if grid[x][y] == '1':
                    print(x,y)
                    self.dfs((x,y))
                    answer += 1
        return answer
        
    def dfs(self, v):
        current_x, current_y = v
        if self.grid[current_x][current_y] == '1':
            self.grid[current_x][current_y] = '0'
            for i in range(4):
                next_x, next_y = current_x+self.dx[i], current_y+self.dy[i]
                if 0<=next_x<self.m and 0<=next_y<self.n and self.grid[next_x][next_y] == '1':
                    self.dfs((next_x,next_y))
        