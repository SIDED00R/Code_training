add_list = [1 for _ in range(1000001)]
for num in range(2, 500001):
    for idx in range(num + num, 1000001, num):
        add_list[idx] += num
ans_list = []
for idx, num in enumerate(add_list):
    ans_list.append(abs(idx - num))

count = 0
while True:
    count += 1
    answer = 0
    start, stop, badness = map(int, input().split())
    if start == stop == badness == 0:
        break
    for i in range(start, stop + 1):
        if ans_list[i] <= badness:
            answer += 1

    print(f"Test {count}: {answer}")
    
    