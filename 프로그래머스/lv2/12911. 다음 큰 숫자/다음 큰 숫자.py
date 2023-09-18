def solution(n):
    give = str(bin(n)).count("1")
    for num in range(n + 1, 1000001):
        find = str(bin(num)).count("1")
        if give == find:
            return num