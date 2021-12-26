import sys
import math
input = sys.stdin.readline

data =[]
maxvalue =0
while True:
    n = int(input())
    maxvalue = max(maxvalue , n)
    if n == 0:
        break
    data.append(n)

prime =[0]*(maxvalue + 1)

for i in range(2,maxvalue+1):
    cnt = 1
    while i * cnt <= maxvalue:
        prime[i*cnt] += 1
        cnt += 1



for i in data:
    result = False
    answer = 0
    for j in range(3 , i //2 +1):
        if prime[j] == 1 and prime[i -j] == 1:
            answer = j
            print(i, end=" = ")
            print(answer, end=" + ")
            print(i - answer)
            result =True
            break
    if result == False:
        print("Goldbach's conjecture is wrong.")

