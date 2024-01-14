grade = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0} 
total_class_down = 0
total_class_top = 0
for _ in range(20):
    a,b,c = input().split()
    b=float(b)
    if c!='P':
        total_class_down += b
        total_class_top += b*grade[c]
print("{0:.6f}".format(total_class_top/total_class_down))
