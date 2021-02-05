
case = 1
while True:
    l, p, v = map(int,input().split())
    if l == 0 and p == 0 and v == 0:
        break
    print(f"Case {case}: {(v % p ) + l * (v // p)}")
    case += 1