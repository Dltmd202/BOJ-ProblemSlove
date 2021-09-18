#2869
#https://www.acmicpc.net/problem/2869
#O(1)
#1 ≤ B < A ≤ V ≤ 1,000,000다,000 때문에 반복문을 사용하면 안된

a , b, v = map(int, input().split())

day = 1
v -= a
day += v /(a-b)

if day - int(day) !=0:
    print(int(day)+1)
else:
    print(int(day))