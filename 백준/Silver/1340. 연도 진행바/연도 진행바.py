month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months = {}
for idx, m in enumerate(month):
    months[m] = idx + 1
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    

line = list(input().split())
now_month = months[line[0]]
dd = int(line[1].rstrip(","))
yy = int(line[2])
if yy % 400 == 0 or (yy % 4 == 0 and yy % 100 != 0):
    total_day = 366
else:
    total_day = 365
    
time = dd - 1 + sum(month_days[:now_month - 1])
if total_day == 366 and now_month > 2:
    time += 1

hh, mm = map(int, line[3].split(":"))

time = time * 24 * 60 + hh * 60 + mm
total_time = total_day * 24 * 60

print(time / total_time * 100)