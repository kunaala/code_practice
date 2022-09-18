from collections import deque

class MinStack:
    def __init__(self):
        self.deq = deque()
        self.minq = deque()      

    def push(self, val: int) -> None:
        self.q.append(val)
        if len(self.deq) == 0:
            self.deq.append(val)
        elif val < self.deq[-1]:
            self.deq.append(val)
        else:
            self.deq.appendleft(val)
            l=0
            while l < len(self.deq)-2 and self.deq[l]<self.deq[l+1]:
                self.deq[l],self.deq[l+1] = self.deq[l+1],self.deq[l]
                l+=1
            # print(self.deq)
        # print("ququq",self.q)

    def pop(self) -> None:
        last = self.q[-1]
        self.q.pop()
        del self.deq[self.deq.index(last)]

    def top(self) -> int:
        # print(self.q)
        return self.q[-1]

    def getMin(self) -> int:
        return self.deq[-1]

class minStack:
    def __init__(self):
        self.stack =[]
        self.minq = []      

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minq) == 0:
            self.minq.append(val)
        elif val < self.minq[-1]:
            self.minq.append(val)
        else:
            self.minq.append(self.minq[-1])
            
        # print(self.minq)
        # print("ququq",self.stack)

    def pop(self) -> None:
        self.stack.pop()
        self.minq.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minq[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()