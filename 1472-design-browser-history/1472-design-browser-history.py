class DoublyLinkedList:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = DoublyLinkedList(homepage)

    def visit(self, url: str) -> None:
        new_node  = DoublyLinkedList(url)
        self.history.next = new_node
        new_node.prev = self.history
        self.history = new_node

    def back(self, steps: int) -> str:
       
        while steps and self.history.prev:
            self.history= self.history.prev
            steps -= 1
        return self.history.val
        
        

    def forward(self, steps: int) -> str:
        
        while steps and self.history.next:
            self.history = self.history.next
            steps -= 1
        return self.history.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)