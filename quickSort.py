def quickSort(a, left, right):
    if left>=right :
        return
    pivot=a[left]
    i=left
    j=right
    while(i<j):
        while(i<j and a[j]>=pivot):
            j=j-1
        while(i<j and a[i]<=pivot):
            i=i+1
        if i<j :
            tmp=a[i]
            a[i]=a[j]
            a[j]=tmp
    a[left]=a[i]
    a[i]=pivot
    quickSort(a,left,i-1)
    quickSort(a,i+1,right)
    return a

if __name__=='__main__':
    a=[3,4,2,7,5,8]
    res=quickSort(a,0,len(a)-1)
    print(res)