class TimeMap:

    def __init__(self):
        self.time_stamp = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in  self.time_stamp:
            self.time_stamp[key] = [(value,timestamp)]
        else:
            self.time_stamp[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        items = self.time_stamp[key]
     
        l,r = 0,len(items)-1
        res = ""
        
        while l <= r:
            mid = l + (r-l)//2
            if items[mid][1] <= timestamp:
                res = items[mid][0]
                l = mid +1
            else:
                r = mid-1
        
            
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)