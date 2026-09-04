class ListNode:
    def __init__(self, key, val, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.capacity = 10**4
        self.arr = [ListNode(-1, -1)] * self.capacity

    def get_index(self, key: int) -> int:
        return key % self.capacity
    def put(self, key: int, val: int) -> None:
        index = self.get_index(key)
        prev = self.arr[index]
        curr = prev.next
        while curr:
            if curr.key == key:
                curr.val = val
                return
            prev = curr
            curr = curr.next
        prev.next = ListNode(key, val)

    def get(self, key: int) -> int:
        index = self.get_index(key)
        prev = self.arr[index]
        curr = prev.next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        index = self.get_index(key)
        prev = self.arr[index]
        curr = prev.next
        while curr and curr.key != key:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)