
class LinkedList:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

Node5 = LinkedList(60, None)
Node4 = LinkedList(40,Node5)
Node3 = LinkedList(20,Node4)
Node2 = LinkedList(10,Node3)
head = LinkedList(5,Node2)

def printNode(Node, n):

    empty = []
    new_list = []
    
    while Node.next != None :
        empty.append(Node.val)
        Node = Node.next

    empty.append(Node.val)

    new_number = len(empty) - n

    new_list = empty[0:new_number] + empty[new_number+1:]

    print(new_list)

    cur = head = LinkedList(0)
    for x in new_list:
        cur.next = LinkedList(x)
        cur = cur.next

    return head.next

