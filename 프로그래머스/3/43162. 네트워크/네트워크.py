# def dfs(computers,visited,node):
#     visited[node]=True
#     for idx,connected in enumerate(computers[node]):
#         if connected and not visited[idx]:
#             dfs(computers,visited,idx)

# def solution(n, computers):
#     answer = 0
#     visited = [False]*n
#     for i in range(n):
#         if not visited[i]:
#             dfs(computers,visited,i)
#             answer += 1
#     return answer
def dfs(computers,visited,node):
    visited[node]=True
    for idx,connected in enumerate(computers[node]):
        # 방문 안했으면 방문해야함
        if not visited[idx] and connected:
            dfs(computers,visited,idx)
def solution(n,computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            dfs(computers,visited,i)
            answer+=1
    return answer