from collections import deque
n = int(input())
apple = int(input())
apples = [list(map(int, input().split())) for _ in range(apple)]
l = int(input())
convert = deque(list(input().split()) for _ in range(l))

head = [1, 1]
snake = deque()
snake.append([1, 1])
turn = 0
direction = 0
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


while True:
    ny = snake[-1][0] + dy[direction]
    nx = snake[-1][1] + dx[direction]
    turn += 1
    if 1 <= ny <= n and 1 <= nx <= n and not [ny, nx] in snake:
        snake.append([ny, nx])
        if not [ny, nx] in apples:
            snake.popleft()
        else:
            apples.remove([ny, nx])
        if convert and turn == int(convert[0][0]):
            if convert[0][1] == 'L':
                direction = (direction + 1) % 4
            else:
                direction = direction - 1 if direction != 0 else 3
            convert.popleft()
    else:
        break
print(turn)