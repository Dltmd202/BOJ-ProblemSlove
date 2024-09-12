
if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))


    A.sort()
    B.sort(reverse=True)
    
    answer = 0
    for a, b in zip(A, B):
        answer += a * b
    print(answer)
