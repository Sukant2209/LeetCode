class ListNode:

    def __init__(self,value=0,next=None):
        self.value = value
        self.next = next

    def link_list(input_list):
        node_list =[]
        node3 = ListNode(input_list[2],None)
        node2 = ListNode(input_list[1],node3)
        node1 = ListNode(input_list[0],node2)
        node_list.append(node1)
        node_list.append(node2)
        node_list.append(node3)
        return node_list

class Solution:

    def addTwoNumber(link_list1,link_list2):
        str1 = ""
        str2= ""
        for x in link_list1:
            str1= str1+str(x.value)
        for x in link_list2:
            str2= str2+str(x.value)
        sum = int(str1) + int(str2)
        print(sum)

input_a = list(map(int,list(input("Enter First list...."))))
input_b = list(map(int,list(input("Enter Second list...."))))

link_list1 = ListNode.link_list(input_a)
link_list2 = ListNode.link_list(input_b)

Solution.addTwoNumber(link_list1,link_list2)       