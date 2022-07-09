# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        
        stack = []
        
        while not head == None:
            stack.append(head.val)
            head = head.next
            
        print(stack)
        
        reverse_stack = stack[::-1]
        
        print(reverse_stack)
        
        len_rs = len(reverse_stack)
        
        head_new  = ListNode(reverse_stack[len_rs - 1], None)
        
        i = len_rs - 2
        
        while  i >= 0 :
            
            head_new = ListNode(reverse_stack[i], head_new)
            i = i - 1
            
        return head_new