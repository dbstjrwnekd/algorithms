class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        travel=collections.defaultdict(list)
        for start, end in sorted(tickets,reverse=True):
            travel[start].append(end)
        answer = []
        
        def dfs(city):
            while travel[city]:
                dfs(travel[city].pop())
            answer.append(city)
            
        dfs('JFK')
        return answer[::-1]