class MyQueue:

    
        
    def __init__(self):
      
        self.addStack, self.popStack = [], []
    def push(self, x):
		# When we add to the queue, we want to add to the addStack
		# if we previously popped, we want to move all items from the popStack to the addStack
        while self.popStack:
            self.addStack.append(self.popStack.pop())
        self.addStack.append(x)  
                    
    def pop(self):
	    # when we pop from the queue, we need to migrate items from addstack to popstack
		# doing this allows us to properly utilize a stack by using the FILO (first in last out) ideology
        while self.addStack:
            self.popStack.append(self.addStack.pop())
        return self.popStack.pop()

    def peek(self):
		# if we previously added, look at the last item in the AddStack
		# if we previously popped, look at the first item in the PopStack
        return self.popStack[-1] if self.popStack else self.addStack[0]

    def empty(self):
		# check to see if either stack has items
        return True if not self.addStack and not self.popStack else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()