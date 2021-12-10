#QUESTION
#https://practice.geeksforgeeks.org/problems/selection-sort/1


class Solution: 
    def select(self, arr, i):
        arr_len = len(arr)
        mini = arr[i]
        min_index = i
        for i in range(i, arr_len):
            if arr[i] < mini:
                mini = arr[i]
                min_index = i
        return min_index
    
    def selectionSort(self, arr,n):
        arr_len = len(arr)
        for i in range(arr_len):
            index = self.select(arr, i)
            arr[i], arr[index] = arr[index], arr[i]
        return arr
