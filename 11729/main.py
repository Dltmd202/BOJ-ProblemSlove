#BOJ 11729

"""
문제
세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다.
이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

입력
첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

출력
첫째 줄에 옮긴 횟수 K를 출력한다.
두 번째 줄부터 수행 과정을 출력한다. 두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데,
이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.
"""

#제한시간 1초
#O(2^n)


n = int(input())
cnt =0
moves = []

def hanoi(n , frm  ,mid, to):
    if n == 0 :
        return

    hanoi(n-1,frm ,to,mid)
    moves.append((frm,to))
    hanoi(n-1,mid,frm,to)


#계산횟수는 2^-1
print(2**n-1)

#함수 호출
hanoi(n,1,2,3)

#출력시간 단축
print('\n'.join(([' '.join(str(step) for step in move) for move in moves])))



