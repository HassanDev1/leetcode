class MyHashSet:

    def __init__(self):
        self.check = {}
        

    def add(self, key: int) -> None:
        if key not in self.check:
            self.check[key] = key
        

    def remove(self, key: int) -> None:
        if key in self.check:
            del self.check[key]
        

    def contains(self, key: int) -> bool:
        return key in self.check
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)