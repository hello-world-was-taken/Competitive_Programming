#QUESTION
#https://www.hackerrank.com/challenges/insertionsort1/problem

#needs refactoring

for i in range(n-1, 0, -1):
        temp = arr[i]
        if temp < arr[i-1]:
            arr[i] = arr[i-1]
            for j in range(n):
                print(arr[j], end=" ")
            print()
            arr[i-1] = temp
        if i==1:
                for j in range(n):
                    print(arr[j], end=" ")
