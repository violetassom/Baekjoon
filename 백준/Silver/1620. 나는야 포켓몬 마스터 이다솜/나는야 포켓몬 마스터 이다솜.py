import sys
m,n = map(int,sys.stdin.readline().split())
pokemon_num = {}
pokemon_chr = {}
for i in range(m):
    pokemon_name = sys.stdin.readline().rstrip()
    pokemon_num[i+1]= pokemon_name
    pokemon_chr[pokemon_name] = i+1
for _ in range(n):
    quiz = sys.stdin.readline().rstrip()
    if quiz.isdigit():
        print(pokemon_num[int(quiz)])
    else:
        print(pokemon_chr[quiz])
    