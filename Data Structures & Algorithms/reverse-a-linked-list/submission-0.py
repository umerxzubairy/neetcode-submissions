# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Problem Statement:
We are given the head of the singly linked list and we need to reverse the linked list and return the updated head.

Clarifying Questions:
1. What if the linked list is empty? we return empty head
2. Do we have to update the values or reverse the memory references? We have to update the memory reference.
3. Is the list ordered? No the list is random

Examples:
 None -> None edge case
 1 -> 2 -> 3 => 3 -> 2 -> 1
 1 -> 1 edge case

Understanding examples:
1 -> 2 -> 3 => None -> 1 -> 2 -> 3
1 -> None 
2 -> 1 -> None
3 -> 2 -> 1 -> None

Approach:
I keep a previous pointer that keep track of the last node visited and I keep track of nextNode and I assign the current node to previous and move the current node to nextNode in the end I return previous because previous would have the lastNode

Plan:
1. prev = None
2. while curr:
    nextNode = curr.next
    curr.next = prev
    prev = curr
    curr = nextNode
3. return prev
'''
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        prev = None
        while head:
            nextNode = head.next
            head.next = prev
            prev = head
            head = nextNode
        return prev