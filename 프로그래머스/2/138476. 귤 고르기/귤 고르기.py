def solution(k, tangerine):
    dic = {}
    ans = []
    for num in tangerine:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
            
    for key, value in dic.items():
        ans.append(value)
    ans = sorted(ans)
    count = 0
    while k > 0:
        k -= ans.pop()
        count += 1
    return count