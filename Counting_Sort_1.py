#QUESTION
#https://www.hackerrank.com/challenges/countingsort1/problem

def countingSort(arr):
    # Write your code here
    arr_len = len(arr)
    new_arr = [0] * 100
    for i in range(arr_len):
        new_arr[arr[i]] += 1
    return new_arr
