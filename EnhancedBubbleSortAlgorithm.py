def enhancedBubbleSort(lst):
    length = len(lst)
    a = []
    for i in range(length-1):
        if(a==[]):
            a.append(0)
        val = a.pop()
        for j in range(val,length-1-i):
            if(lst[j]>lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
            else:
                a.append(j)
    return lst
print(enhancedBubbleSort([2, 4, 29, 22, 15, 17]))
