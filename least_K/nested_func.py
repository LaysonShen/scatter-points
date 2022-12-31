class Solution:

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        def heapify(k, i):
            c1 = 2 * i + 1
            c2 = 2 * i + 2
            max = i
            if c1 < k and arr[c1] > arr[max]:
                max = c1
            if c2 < k and arr[c2] > arr[max]:
                max = c2
            if max != i:
                arr[i], arr[max] = arr[max], arr[i]
                heapify(k, max)

        if k == 0 or len(arr) == 0:
            return []
        n = len(arr)
        for i in range((k - 2) // 2, -1, -1):
            heapify(k, i)

        for i in range(k, n):
            if arr[0] > arr[i]:
                arr[0] = arr[i]
                heapify(k, 0)
        return arr[:k]