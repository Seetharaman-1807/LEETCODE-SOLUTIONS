class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case: if list is empty or has only one node, it is already sorted
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into two halves
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        # Step 2: Recursively sort both halves
        left = self.sortList(left)
        right = self.sortList(right)
        
        # Step 3: Merge the sorted halves
        return self.merge(left, right)
    
    def getMid(self, head: ListNode) -> ListNode:
        # Fast and slow pointer approach to find the middle node
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def merge(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Dummy node to easily handle the head of the merged list
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        # Append any remaining nodes
        if list1:
            tail.next = list1
            
        if list2:
            tail.next = list2
            
        return dummy.next
