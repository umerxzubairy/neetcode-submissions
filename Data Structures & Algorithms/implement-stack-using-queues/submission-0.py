'''
initialize => []
empty => true   []
push 1 =>       [1]
push 2 =>       [1,2]
top => 2        [1,2]
empty => false  [1,2]
push 3 =>       [1,2, 3]
pop => 3        [1,2]
push 4          [1,2,4]
top => 4        [1,2,4]
pop => 4        [1,2]
pop => 2        [1]
pop => 1        []
empty => true

[], [] both are empty so true
[1], [] push into first stack
[1,2], [] push into the first stack
[2], [1] => [1,2], [] we dequeu elements from 1 and enqueu into 2 and record the last element and then assign first to second and second to first
[1,2], [] since first is not empty so false
[1,2,3], [] we insert into the first q
[3], [1,2] we dequeu from first until we have one element left and then we dequeu last element and then we assign second to first

'''
from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque([])
        self.q2 = deque([])

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if self.empty():
            return -1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        num =  self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return num

    def top(self) -> int:
        if self.empty():
            return -1
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        num =  self.q1.popleft()
        self.q2.append(num)
        self.q1, self.q2 = self.q2, self.q1
        return num


    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()