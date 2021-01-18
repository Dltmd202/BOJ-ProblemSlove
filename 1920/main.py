#1920
#BinarySearch
#Sort Libary O(N*logN)
#BinarySearch O(N*logN)

n = int(input())

a = list(map(int,input().split()))
a.sort()

m = int(input())
data = list(map(int,input().split()))

visit = [0]*(m)

def bisearch(left ,right,target):
    if left > right:
        return -1

    mid = (left+right)//2

    if a[mid] == target:
        return mid

    elif a[mid] < target:
        return bisearch(mid+1,right,target)
    else:
        return bisearch(left,mid-1,target)



for i in range(m):
    visit[i] = 1 if bisearch(0,n-1,data[i]) != -1 else 0

for i in visit:
    print(i)

