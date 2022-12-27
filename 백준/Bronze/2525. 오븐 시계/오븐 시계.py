input_hour, input_minute = map(int, input().split())
plus_minute = int(input())

if input_hour == 0:
    input_hour = 24

input_time = input_hour * 60 + input_minute
plused_time = input_time + plus_minute

output_hour = plused_time//60
output_minute = plused_time%60

print(output_hour%24,output_minute)
