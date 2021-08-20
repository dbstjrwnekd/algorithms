import collections
DEFAULT_VALUE = 65536

def solution(str1, str2):
    answer = 0
    set_1, set_2 = get_default_sets([str1, str2])
    
    if not set_1 and not set_2:
        return DEFAULT_VALUE
    
    answer = get_jaccard(set_1, set_2)
    
    return int(answer*DEFAULT_VALUE)

def get_default_sets(strings):
    default_sets = []
    for string in strings:
        default_sets.append(get_default_set(string))
    return default_sets
            
def get_default_set(string):
    default_set = collections.defaultdict(int)
    for i in range(len(string)-1):
        word = string[i:i+2]
        if word.isalpha():
            word = word.lower()
            default_set[word] += 1
    return default_set

def get_jaccard(set_1, set_2):
    intersection, union = get_default_sets(['',''])
    
    for ch in set_1:
        if ch in set_2:
            intersection[ch] = min(set_1[ch], set_2[ch])
            union[ch] = max(set_1[ch], set_2[ch])
            del set_2[ch]
            continue
        union[ch] = set_1[ch]
    
    for ch in set_2:
        union[ch] = set_2[ch]
        
    inter, uni = sum(intersection.values()), sum(union.values())
    
    return inter/uni
            