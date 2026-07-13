# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None
        
        newarr = []

        for li in lists:
            temp = li
            while temp:
                newarr.append(temp.val)
                temp= temp.next
        newarr.sort()

        newhead = ListNode()
        curr= newhead
        for i in newarr:
            curr.next = ListNode(i)
            curr= curr.next
        return newhead.next