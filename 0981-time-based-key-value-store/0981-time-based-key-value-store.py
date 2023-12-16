class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        items = self.cache[key]
        l,r = 0,len(items)-1
        
        while l <= r:
            mid = l+ (r-l)//2
            if items[mid][1] <= timestamp:
                res = items[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)