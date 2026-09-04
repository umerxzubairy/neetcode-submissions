class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.capacity = 10**4
        self.arr = [ListNode(0)] * self.capacity

    def add(self, key: int) -> None:
        index = key % self.capacity
        prev = self.arr[index]
        curr = prev.next
        while curr:
            if curr.val == key:
                return
            prev = curr
            curr = curr.next
        prev.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = key % self.capacity
        prev = self.arr[index]
        curr = prev.next
        while curr and curr.val != key:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next

    def contains(self, key: int) -> bool:
        index = key % self.capacity
        curr = self.arr[index].next
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)