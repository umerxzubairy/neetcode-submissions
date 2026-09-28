# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Problem Statement:
Two linkedlist are given and both are sorted, we need to merge the two linked list and give a sorted linked list

Clarifying Questions:
1. Can there be empty linked list in either? yes its possible that either both are empty or either is empty or both are full
2. When we have equal number in both lists is there are preference on which one to choose? No you can choose either as long as the output is sorted.

Examples
l1 = [1] l2 = [2] =>[ 1 -> 2]
l1 = [] l2 = [2] => [2]edge case
l1 = [] l2 = [] => [] edge case

Understanding the example:
1 -> 2 -> 4
1 -> 3 -> 5


Approach: 
We can create a dummy node and then while we have both the list we can keep comparing which list elements is larger if its list one we make it dummy.next and prompte it to dummy and then move the pointer if its list two we do it the same
while the list1 is empty but list 2 is not empty we assing the entire list to dummy.next 
while the list2 is empty but list1 is not empty we assign the entire list to dummy.next
return the dummy.next
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        dummy = ListNode(-1)
        root = dummy
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        return root.next

        