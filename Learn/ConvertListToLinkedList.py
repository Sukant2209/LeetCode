
class LinkedList:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

listToConvert = [1,4,7,8]

def qwer(listToConvert):
    cur = head = LinkedList(0)
    for x in listToConvert:
        cur.next = LinkedList(x)
        cur = cur.next
    return head.next

result = qwer(listToConvert)
print(result.next.next.next.next)


