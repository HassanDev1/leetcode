class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        time = 0
        heap = []
        count = Counter(tasks)
        for k,v in count.items():
            heappush(heap,-v)
            
        q = deque()
        
        while heap or q:
            time += 1
            if heap:
                cnt  = 1 + heappop(heap)
                
                if cnt:
                    q.append((cnt,n+time))
                    
            if q and q[0][1] == time:
                heappush(heap,q.popleft()[0])
                
        return time
                