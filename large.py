import sys, string, math
N = int(input())
l = list(map(int,input().split()))
l1 = sorted(l)
k = len(l)
#print(l,l1,k)
sum1 = L1[0]
a = 10
for i in range(1,len(L1)) :
    sum1 = sum1 + L1[i]*a
    a = a*10
print(sum1)
