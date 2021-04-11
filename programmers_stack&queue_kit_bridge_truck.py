import collections

def solution(bridge_length, weight, truck_weights):
    #pop(0)는 O(n)이므로 deque로 변형
    bridge = collections.deque([])
    truck_weights = collections.deque(truck_weights)

		#weight계산용 (sum은 오래걸림)
    cur_weight = 0
    answer = 0
    
    while True:
				#길이가 최대이면 맨 앞의 요소를 제거
        if len(bridge) == bridge_length:
            truck = bridge.popleft()
            cur_weight -= truck
        #올릴 수 있으면 새로 올리고, 안되면 0을 추가
        if truck_weights[0] + cur_weight <= weight:
            truck = truck_weights.popleft()
            bridge.append(truck)
            cur_weight += truck
        else:
            bridge.append(0)
				#싸이클마다 time1초 증가
        answer += 1
        #마지막 트럭이 올라가면 중지
        if len(truck_weights) == 0:
            break
    #계산한 결과에 마지막 트럭이 지나가는 시간(bridge_length)를 더해서 return
    return answer + bridge_length