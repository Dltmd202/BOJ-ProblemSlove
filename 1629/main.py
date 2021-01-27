a , b, c = map(int,input().split())

answer = 1

for i in range(b):
    answer = (answer * a) % c
print(answer)