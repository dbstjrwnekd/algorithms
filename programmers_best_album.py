import collections
import heapq

def solution(genres, plays):
    answer = []
    genreCount = collections.defaultdict(int)
    genreTable = collections.defaultdict(list)
    
    for i, play in enumerate(plays):
        genre = genres[i]
        genreCount[genre] += play
        heapq.heappush(genreTable[genre], (-1*play, i))
    
    for genre in sorted(genreCount.keys(), key=lambda x: -1*genreCount[x]):
        songs = heapq.nsmallest(2,genreTable[genre])
        for _, num in songs:
            answer.append(num)
    
    return answer
    