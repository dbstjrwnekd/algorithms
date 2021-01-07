class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if src == dst:
            return 0
        graph = collections.defaultdict(list)
        for start, end, price in flights:
            graph[start].append((end,price))
        
        Q = [(0,src,K)]
        
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            
            if k >= 0:
                for w, v in graph[node]:
                    alt = v+price
                    heapq.heappush(Q,(alt,w,k-1))
        
        return -1