list1 = [3,4,1,6,2,6,8]

def bubbleSort(list1):
    l = len(list1)-1
    for i in range(l-1):
        for j in range(0,l-i-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
    return list1

print(bubbleSort(list1))