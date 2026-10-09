class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        maximum = arr[-1]
        arr[-1] = -1

        for i in range(len(arr) - 2, -1, -1):
            current = arr[i]
            arr[i] = maximum
            maximum = max(maximum, current)

        return arr
        
        