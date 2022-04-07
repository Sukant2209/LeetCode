list1 = [1, 40,90]
list2 = [3, 4, 7, 8, 10]

sortedlist =[]

i=0;j=0
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j] :
        sortedlist.append(list1[i])
        i=i+1
    else:
        sortedlist.append(list2[j])
        j=j+1
    
sortedlist = sortedlist + list1[i:] + list2[j:]

print(sortedlist)



