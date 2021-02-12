

dot =[]

for i in range(3):
    dot.append(tuple(map(int,input().split())))

def ccw(dot):
    a, b, c = dot
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    pre = (x1 * y2 + x2 *y3 + x3 * y1)
    post = (x2 * y1 + x3 * y2 + x1 * y3)
    if pre - post > 0:
        return 1
    elif pre - post == 0:
        return 0
    elif pre - post < 0:
        return -1

print(ccw(dot))