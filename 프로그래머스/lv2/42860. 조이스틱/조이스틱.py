def solution(name):
    # 글자를 바꿔야 하는 횟수로 치환
    letter = []
    for alp in name:
        num = ord(alp) - 65
        if num > 13:
            num = 91 - ord(alp)
        letter.append(num)
    
    answer = []
    
    for i in range(len(letter)):
        a = letter[:]
        b = [0 for _ in range(len(a))]
        count, move, ans = 0, 0, 0
        find = False
        while move < i:
            ans += a[move]
            a[move] = 0
            if a == b:
                find = True
                break
            move += 1
            count += 1
            
        ans += count
        count = 0
        
        while not find:
            ans += a[move]
            a[move] = 0
            if a == b:
                find = True
                break
            move -= 1
            count += 1
            
        answer.append(ans + count)
        
        a = letter[:]
        count, move, ans = 0, 0, 0
        find = False
        
        while -move < i:
            ans += a[move]
            a[move] = 0
            if a == b:
                find = True
                break
            move -= 1
            count += 1

        ans += count
        count = 0
        
        while not find:
            ans += a[move]
            a[move] = 0
            if a == b:
                find = True
                break
            move += 1
            count += 1
            
        answer.append(ans + count)
        
    return min(answer)