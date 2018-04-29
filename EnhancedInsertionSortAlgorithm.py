def enhancedInsertionSort(a):
    length = len(a)
    b=[]
    for i in range(0,2*length):
        b.append(None)
    left = length
    right = length
    b[left] = a[0]
    for i in range(1,length):
        if(a[i]>=b[right]):
            right = right + 1
            b[right]=a[i]
            continue
        if(a[i]<=b[left]):
            left = left-1
            b[left] = a[i]
            continue
        loc = right
        while (a[i]<b[loc]):
            loc = loc-1
        if (right-loc<loc-left):
            j=right+1
            while (j>loc+1):
                b[j]=b[j-1]
                j=j-1
            right=right+1
            b[loc+1]=a[i]
        else:
            j=left-1
            while (j<loc):
                b[j]=b[j+1]
                j=j+1
            left = left-1
            b[loc] = a[i]
    for i in range(0,length):
        a[i]=b[left]
        left = left+1
    return a

print(enhancedInsertionSort([2, 4, 29, 22, 15, 17]))

            
