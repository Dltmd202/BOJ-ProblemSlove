n = input()
fix = set()

for i in range(len(n)):
    fix.add(n[i:])

fix = list(fix)
fix.sort()
print('\n'.join(word for word in fix))