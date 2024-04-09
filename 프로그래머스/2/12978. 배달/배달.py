from collections import deque
def solution(N, road, K):
    answer = 0
    
    
    # 탐색 그래프를 만든다
    graph = []
    for i in range(N+1):
        graph.append([])
        
    for start,end,time in road:
        graph[start].append((end,time))
        graph[end].append((start,time))
        
    # 시간 리스트 만들기
    road_time = [float('inf')]*(N+1)
    
    # 첫번째 마을은 0
    road_time[1]=0
    # 탐색 시작할 시점
    queue = deque([(1,0)])
    time = 0
    # 탐색
    while queue:
        current_town,current_time = queue.popleft()
        for delivery_town,time in graph[current_town]:
            delivery_time = current_time+time
            if delivery_time < road_time[delivery_town]:
                road_time[delivery_town] = delivery_time
                queue.append((delivery_town,delivery_time))
    for i in road_time:
        if i <= K:
            answer+=1

    return answer