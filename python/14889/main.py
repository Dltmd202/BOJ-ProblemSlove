#14889
#https://www.acmicpc.net/problem/14889

n = int(input())

graph = []
firstTeamMember = [False]*(n+1)
for i in range(n):
    data = list(map(int,input().split()))
    graph.append(data)


answer = int(1e9)



def count(data : list,visit : list, select :list, m,idx):
    if m == 0:
        return graph[select[0]-1][select[1]-1]+graph[select[1]-1][select[0]-1]

    ret = 0
    for i in range(idx,len(data)):
        if not visit[i]:
            select.append(data[i])
            visit[i] = True
            ret += count(data,visit,select,m-1,i)
            visit[i]= False
            select.pop()
    return ret


def solution(firstTeam : list , m , idx):
    if m == 0:
        global answer
        first = count(firstTeam,[False] * (len(firstTeam)+1) , [] , 2, 0)
        secondTeam = []
        for i in range(n):
            if i not in firstTeam:
                secondTeam.append(i)
        second = count(secondTeam , [False] * (len(secondTeam)+1) , [] ,2 ,0)
        answer = min(answer , abs(first-second))

    for i in range(idx , n):
        if not firstTeamMember[i]:
            firstTeam.append(i)
            firstTeamMember[i] = True
            solution(firstTeam , m-1 ,i)
            firstTeam.pop()
            firstTeamMember[i] = False

solution([],n//2,0)
print(answer)