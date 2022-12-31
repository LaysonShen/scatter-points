class Solution:
    def getLeastNumbers(self,arr:List[int],k:int)->List[int]:
        if k==0 or len(arr)==0:
            return []
        n=len(arr)
        nums=arr[:k]
        self.buildHeap(nums,k)

        for i in range(k,n):
            if nums[0]>arr[i]:
                nums[0]= arr[i]
                self.heapify(nums,k,0)
        return nums

    def swap(self,arr,i,j):
        arr[i],arr[j]=arr[j],arr[i]

    def buildHeap(self,arr,k):
        for i in range((k-2)//2,-1,-1):
            self.heapify(arr,k,i)

    def heapify(self,arr,k,i):
        c1=2*i+1
        c2=2*i+2
        max=i
        if c1<k and arr[c1]>arr[max]:
            max=c1
        if c2<k and arr[c2]>arr[max]:
            max=c2
        if max!=i:
            self.swap(arr,max,i)
            self.heapify(arr,k,max)