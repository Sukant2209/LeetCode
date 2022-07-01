class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        e1 = []
        e2 = []
        
        while not l1.next == None:
            e1.append(l1.val)
            l1 = l1.next
        e1.append(l1.val)
        
        while not l2.next == None:
            e2.append(l2.val)
            l2 = l2.next
        e2.append(l2.val)
        
        num1 = 0
        num2 = 0
        
        for i in range(len(e1)):
            num1 = num1 + (e1[i] * (10 **i))
        for i in range(len(e2)):
            num2 = num2 + (e2[i] * (10 ** i))
            
        sum = str(num1 + num2)[::-1]
        
        sum_list = list(map(int,list(sum)))
        
        if len(sum_list) == 1:
            head = ListNode(val=sum_list[0],next=None)
            return head
        
        tail = ListNode(sum_list[len(sum_list)-1],None)

        for i in range(len(sum_list)-2, -1, -1):
                if i == 0:
                    node = (ListNode(sum_list[i], tail))
                else:
                    node = ListNode(sum_list[i],tail)

                tail = node
        
        return node
   
        

# num1 = ""
#         num2 = ""
        
#         while not l1.next == None:
#             num1 = num1 + str(l1.val)
#             l1 = l1.next
#         num1 = num1 + str(l1.val)
        
#         while not l2.next == None:
#             num2 = num2 + str(l2.val)
#             l2 = l2.next
#         num2 = num2 + str(l2.val)
     
        
#         sum = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
       
#         sum_list = list(map(int,list(sum)))
        
#         if len(sum_list) == 1:
#             head = ListNode(val=sum_list[0],next=None)
#             return head
        
#         tail = ListNode(sum_list[len(sum_list)-1],None)

#         for i in range(len(sum_list)-2, -1, -1):
#                 if i == 0:
#                     node = (ListNode(sum_list[i], tail))
#                 else:
#                     node = ListNode(sum_list[i],tail)

#                 tail = node
        
#         return node
   