class MyQueue:
    def __init__(self):
        self. accpectstack = []
        self. outputstack = []

    def push(self, a: int):  #将一个元素放入队列的尾部。
        self.accpectstack.append(a)

    def pop(self) -> int:  #从队列首部移除元素。
        while len(self.accpectstack) > 1:
            self.outputstack.append(self.accpectstack.pop())
        res = self.accpectstack.pop()
        while len(self.outputstack) > 0:
            self.accpectstack.append(self.outputstack.pop())
        return res

    def peek(self) -> int:  #返回队列首部的元素。
        return self.accpectstack[0]

    def empty(self) -> bool:  #返回队列是否为空。
        return len(self.accpectstack) == 0
myqueue = MyQueue()
myqueue.push(1)
myqueue.push(2)
myqueue.push(3)
print(myqueue.pop())
print(myqueue.peek())
print(myqueue.empty())