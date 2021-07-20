import collections

def solution(N, stages):
    #각 스테이지별 인원수를 표시하는 stage_table 생성 - list
    stage_table = create_stage_table(N, stages)
    #각 스테이지별 실패율을 계산한 complete_rate 생성 - dict
    complete_rate = get_complete_rate(N, stage_table)
    #complete_rate을 이용해 순서를 계산
    answer = calculate_answer(complete_rate)
    
    return answer

def create_stage_table(N, stages):
    stage_table = [0] * (N+2)
    
    for stage in stages:
        stage_table[stage] += 1
        
    return stage_table

def get_complete_rate(N, stage_table):
    complete_rate = collections.defaultdict(int)
        
    for i in range(1,N+1):
        arise_num = sum(stage_table[i:])
        if arise_num != 0:
            complete_rate[i] = stage_table[i] / arise_num
        else:
            complete_rate[i] = 0
            
    return complete_rate

def calculate_answer(complete_rate):
    answer = list(complete_rate.keys())
    answer.sort(key = lambda x : (-complete_rate[x], x))
    
    return answer
