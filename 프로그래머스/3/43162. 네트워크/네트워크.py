def solution(n, computers):
    visited = [0]*n
    def dfs(visited,node):
        if visited[node]==0:
            visited[node]=1
            for i in range(n):
                if visited[i]==0 and computers[node][i]==1:
                    dfs(visited,i)
    answer = 0
    for j in range(n):
        if visited[j]==0:
            dfs(visited,j)
            answer+=1
            
    return answer