class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.head.next = new_node
        new_node.prev = self.head
        self.head = new_node

    def back(self, steps: int) -> str:
        
        while steps and self.head.prev:
            self.head = self.head.prev
            steps -= 1
        return self.head.val
        

    def forward(self, steps: int) -> str:
        
        while steps and self.head.next:
            self.head = self.head.next
            steps -= 1
        return self.head.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)