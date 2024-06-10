from collections import deque
def solution(maps):
    move = [[-1,0],[0,-1],[0,1],[1,0]]
    
    n=len(maps)
    m=len(maps[0])
    
    dist = [[-1]*m for _ in range(n)]
    
#     def bfs(start):
#         q=deque([start])
#         dist[start[0]][start[1]]=1
#         while q:
#             print('q',q)
#             here = q.popleft()
#             for direct in move:
#                 row,column = here[0]+direct[0],here[1]+direct[1]
#                 if row<0 or row>=n or column <0 or column >= m:
#                     continue
#                 if maps[row][column]==0:
#                     continue
#                 if dist[row][column]==-1:
#                     print('row',row,'col',column)
#                     q.append([row,column])
#                     dist[row][column]=dist[here[0]][here[1]]+1
#             print('for 끝')
#         return dist
    def bfs(start):
        q = deque([start])
        dist[start[0]][start[1]]=1
        while q:
            here = q.popleft()
            for i,j in move:
                row,col = here[0]+i,here[1]+j
                if row<0 or row>=n or col<0 or col>=m:
                    continue
                if maps[row][col]==0:
                    continue
                if dist[row][col]==-1:
                    q.append([row,col])
                    dist[row][col]=dist[here[0]][here[1]]+1
        return dist
            
    bfs([0,0])
    # print(*dist,sep='\n')
    return dist[n-1][m-1]
            
                
    answer = 0
    return answer