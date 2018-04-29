def enhancedSelectionSort(lst):
    length = len(lst)
    s = []
    while(length!=1):
        if(s==[]): 
            s.append(0)
        maximum = s.pop()
        count = maximum+1
        while(count<length):
            if(lst[count]>lst[maximum]):
                lst[count-1],lst[maximum] = lst[maximum], lst[count-1]
                s.append(count-1)
                maximum = count
            count = count+1
        lst[length-1], lst[maximum] = lst[maximum], lst[length-1]
        length = length - 1
    return lst
print(enhancedSelectionSort([2, 4, 29, 22, 15, 17]))
