counts = int(input())
for i in range(counts):
    a,b = input().split()
    for j in b:
        print(j*int(a),end="")
    print()