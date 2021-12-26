from itertools import product

for tb in range(int(input())):
    n = int(input())
    cnt =0
    pos = [1,2,3]

    def solution(sum):
        global cnt
        if sum == n:
            cnt += 1
        elif sum < n:
            for i in range(3):
                solution(sum + pos[i])
    solution(0)
    print(cnt)
