from collections import defaultdict
import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = defaultdict(Node)
        self.res = False


class Boggle:
    def __init__(self, N):
        self.root = Node()
        self.N = N
        self.dx = [-1, -1, -1, 0, 0, 1, 1, 1]
        self.dy = [1, -1, 0, 1, -1, 1, -1, 0]
        self.result = set()

    def makeTrie(self, temp):
        node = self.root
        for char in temp:
            node = node.children[char]
            node.data = char
        node.res = True

    def wordInput(self):
        for i in range(self.N):
            temp = input().strip()
            self.makeTrie(temp)

    def myBoard(self):
        board = []
        for _ in range(4):
            board.append(list(input().strip()))
        return board

    def findWord(self, board, y, x, visit, word, node):
        word += board[y][x]
        if node.res:
            self.result.add(word)
        visit[y][x] = True
        for k in range(8):
            nx = x + self.dx[k]
            ny = y + self.dy[k]
            if 0 <= nx <= 3 and 0 <= ny <= 3:
                if not visit[ny][nx] and board[ny][nx] in node.children:
                    self.findWord(board, ny, nx, visit, word, node.children[board[ny][nx]])
                    visit[ny][nx] = False

    def printAnswer(self):
        point = str(self.checkPoint())
        maxWord = self.checkMaxWord()
        cnt = str(len(self.result))
        return point + " " + maxWord + " " + cnt

    def checkPoint(self):
        point = 0
        for i in self.result:
            if len(i) < 3:
                continue
            elif len(i) < 5:
                point += 1
            elif len(i) == 5:
                point += 2
            elif len(i) == 6:
                point += 3
            elif len(i) == 7:
                point += 5
            elif len(i) == 8:
                point += 11
        return point

    def checkMaxWord(self):
        temp = sorted(self.result, key=lambda x: (-len(x), x))
        return temp[0]

    def solution(self):
        board = self.myBoard()
        self.result.clear()
        for i in range(4):
            for j in range(4):
                visit = [[False] * 4 for _ in range(4)]
                if board[i][j] in self.root.children:
                    node = self.root.children[board[i][j]]
                    self.findWord(board, i, j, visit, "", node)
        print(self.printAnswer())


N = int(input())
test = Boggle(N)
test.wordInput()
input().rstrip()
K = int(input())
test.solution()
for _ in range(K - 1):
    input()
    test.solution()