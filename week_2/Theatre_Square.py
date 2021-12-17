#QUESTION
#https://codeforces.com/problemset/problem/1/A

from math import ceil 

n,m,a=input().split() 

n = int(n)
m = int(m)
a = int(a)  
c = ceil(n/a)*ceil(m/a)  

print(c)
