def solution(n, k, cmd):
    linked_list = [["no", "O", 1]] + [[i, "O", i + 2] for i in range(n - 2)] + [[n - 2, "O", "no"]]
    now = k
    stack = []
    
    for action in cmd:
        
        if action == "C":
            back = linked_list[now][0]
            front = linked_list[now][2]
            linked_list[now][1] = "X"
            
            if back != "no":
                linked_list[back][2] = front
            stack.append(now)
            if front == "no":
                now = back
            else:
                linked_list[front][0] = back
                now = front
            
        elif action == "Z":
            index = stack.pop()
            back = linked_list[index][0]
            front = linked_list[index][2]
            
            linked_list[index][1] = "O"
            
            if back != "no":
                linked_list[back][2] = index
            
            if front != "no":
                linked_list[front][0] = index

        else:
            move, num = action.split()
            num = int(num)
            if move == "D":
                for _ in range(num):
                    now = linked_list[now][2]
            else:
                for _ in range(num):
                    now = linked_list[now][0]
                    
    answer = ""
    
    for block in linked_list:
        answer += block[1]
                
    return answer