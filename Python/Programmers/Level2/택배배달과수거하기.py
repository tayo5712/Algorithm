def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries and not deliveries[-1]:
        deliveries.pop()
    while pickups and not pickups[-1]:
        pickups.pop()
    
    while deliveries or pickups:
        answer += max(len(deliveries), len(pickups)) * 2
        dc = pc = cap
        while deliveries:
            if deliveries[-1] <= dc:
                dc -= deliveries.pop()
            else:
                deliveries[-1] -= dc
                break
        while pickups:
            if pickups[-1] <= pc:
                pc -= pickups.pop()
            else:
                pickups[-1] -= pc
                break
      
    return answer
