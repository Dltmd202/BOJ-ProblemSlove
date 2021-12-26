#14888
#https://www.acmicpc.net/problem/14888


n = int(input())

data = list(map(int,input().split()))
ins = list(map(int,input().split()))

max = int(-1e10)
min = int(1e10)

def solution(select : list , m):
    global max
    global min
    if sum(ins) == 0:
        result = data[0]
        for i in range(len(select)):
            if select[i] == 0 :
                result += data[i+1]
            elif select[i] == 1 :
                result -= data[i+1]
            elif select[i] == 2 :
                if result >= 0:
                    result *= data[i+1]
                else :
                    result = -(-result * data[i+1])
            elif select[i] == 3 :
                if result >= 0:
                    result //= data[i+1]
                else :
                    result = -(-result // data[i+1])

        if max < result :
            max = result
        if min > result:
            min = result
        return

    for i in range(4):
        for j in range(ins[i]):
            ins[i] -= 1
            select.append(i)
            solution(select,m-1)
            ins[i] += 1
            select.pop()

solution([],n-1 )

print(max)
print(min)
