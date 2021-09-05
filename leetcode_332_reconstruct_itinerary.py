class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        initCity = 'JFK'
        ticketTable = collections.defaultdict(list)
        for start, end in sorted(tickets, reverse=True):
            ticketTable[start].append(end)
            
        answer = []
        
        def dfs(city):
            while ticketTable[city]:
                dfs(ticketTable[city].pop())
            answer.append(city)
            
        dfs(initCity)
        
        return answer[::-1]
    