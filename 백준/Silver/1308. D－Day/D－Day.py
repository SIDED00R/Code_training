today = list(map(int, input().split()))
dday = list(map(int, input().split()))

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def count_day(time):
    year, month, day = time
    total_day = 0
    total_day += 365 * (year - 1)
    total_day += (year - 1) // 4
    total_day -= (year - 1) // 100
    total_day += (year - 1) // 400
    total_day += sum(months[:month])
    if month > 2 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        total_day += 1
    total_day += day
    return total_day

now = count_day(today)
gg = today[:]
gg[0] += 1000
d_day = count_day(dday)
if d_day >= count_day(gg):
    print("gg")
else:
    print(f"D-{d_day - now}")
    