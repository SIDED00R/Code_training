def solution(bridge_length, weight, truck_weights):
    bridge = [0 for _ in range(bridge_length)]
    truckidx = 0
    answer = 0
    total = 0
    
    while len(truck_weights) != truckidx:
        out = bridge.pop(0)
        total -= out
        if total + truck_weights[truckidx] <= weight:
            bridge.append(truck_weights[truckidx])
            total += truck_weights[truckidx]
            truckidx += 1
        else:
            bridge.append(0)
        answer += 1
        
    return answer + bridge_length