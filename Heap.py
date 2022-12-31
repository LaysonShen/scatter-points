def swap(a,i,j):
    tmp=a[i]
    a[i]=a[j]
    a[j]=tmp

def heapify(tree,n,i):
    c1=2*i+1
    c2=2*i+2
    max=i
    if c1<n and tree[c1]>tree[max]:
        max=c1
    if c2<n and tree[c2]>tree[max]:
        max=c2
    if max!=i:
        swap(tree,max,i)
        heapify(tree,n,max)

def build_heap(tree,n):
    parent=(n-2)//2
    for i in range(parent,-1,-1):
        print("i",i)
        heapify(tree,n,i)

def heap_sort(tree,n):
    build_heap(tree,n)
    for j in range(n-1,-1,-1):
        swap(tree,j,0)
        heapify(tree,j,0)

if __name__ =='__main__':
    tree=[10,5,8,3,9,4,6,7,1,2]
    n=len(tree)
    heap_sort(tree,n)
    print("tree:",tree)