def solution(dirs):
    def is_valid(npoint):
        nx,ny = npoint
        return -5<=nx<=5 and -5<=ny<=5
    def switch(npoint):
        nx,ny = npoint
        if i=="U":
            ny+=1
        if i=="D":
            ny-=1
        if i=="L":
            nx-=1
        if i=="R":
            nx+=1
        return (nx,ny)
    x = 0
    y = 0
    start = (x,y)
    route = []
    for i in dirs:
        end = switch(start)
        if is_valid(end):
            route.append((start,end))
            route.append((end,start))
            start = end
    answer = len(set(route))//2
    return answer