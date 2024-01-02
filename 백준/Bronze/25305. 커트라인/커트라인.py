#5 2
#100 76 85 93 98

#98

import sys
a,b = map(int, sys.stdin.readline().split())
score = list(map(int,sys.stdin.readline().split()))
score.sort(reverse=True)
print(score[b-1])