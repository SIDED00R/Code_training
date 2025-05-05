while True:
    n = int(input())
    if n == 0:
        break
    dic = {}
    first_name = ""
    for i in range(n):
        k, v = input().split(':')
        if i == 0:
            first_name = k
        value = list(v[:-1].split(','))
        dic[k] = value

    name = set()
    stack = set()
    stack.update(dic[first_name])
    while stack:
        next_stack = set()
        for now_case in stack:
            if now_case in dic:
                next_stack.update(dic[now_case])
            else:
                name.add(now_case)
        stack = next_stack.copy()
    
    print(len(name))

