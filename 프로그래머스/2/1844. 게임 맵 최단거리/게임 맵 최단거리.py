from collections import deque
def solution(maps):
    moves = [[1,0],[0,1],[-1,0],[0,-1]]
    n = len(maps)
    m = len(maps[0])
    
    trace = [[0]*m for _ in range(n)]
    def bfs(start_x,start_y):
        queue = deque([(start_x,start_y)])
        trace[start_x][start_y]=1
        while queue:
            q = queue.popleft()
            here_x,here_y = q
            for move in moves:
                new_x,new_y = here_x+move[0],here_y+move[1]
                if new_x<0 or new_x>=n or new_y<0 or new_y>=m:
                    continue
                if maps[new_x][new_y]==0:
                    continue
                if trace[new_x][new_y]!=0:
                    continue
                trace[new_x][new_y]=trace[here_x][here_y]+1
                if new_x==n-1 and new_y==m-1:
                    return trace[new_x][new_y]
                queue.append((new_x,new_y))
        return -1
    
    
    answer = bfs(0,0)
    return answer