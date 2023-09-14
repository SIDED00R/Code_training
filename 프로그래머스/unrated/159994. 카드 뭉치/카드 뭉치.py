def solution(cards1, cards2, goal):
    card = "c1"
    count = 0
    
    while len(goal) != 0:
        if card == "c1":
            if cards1[0] == goal[0]:
                cards1.pop(0)
                goal.pop(0)
                count = 0
            else:
                card = "c2"
                count += 1
            if len(cards1) == 0:
                card = "c2"
                count += 1
                
        elif card == "c2":
            
            if cards2[0] == goal[0]:
                cards2.pop(0)
                goal.pop(0)
                count = 0
            else:
                card = "c1"
                count += 1

            if len(cards2) == 0:
                card = "c1"
                count += 1
        if len(goal) == 0:
            break
        if count == 3:
            return "No"
        if card == "c1" and len(cards1) == 0:
            return "No"
        elif card == "c2" and len(cards2) == 0:
            return "No"
        
    
    return "Yes"