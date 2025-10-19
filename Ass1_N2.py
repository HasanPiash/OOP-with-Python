# import sys
# input = sys.stdin.read
# data = input().split()
# N = 100100
# n = int(data[0])
# a = [0] * N
# ans = 0

# for i in range(1, n + 1):
#     x = int(data[i])
#     if x >= N:
#         ans += 1
#     else:
#         a[x] += 1

# for i in range(1, N):
#     if a[i] < i:
#         ans += a[i]
#     else:
#         ans += a[i] - i
# print(ans)


N=100100
n=int(input().strip())
a=[0]*N
ans=0
data=list(map(int,input().strip().split()))
for x in data:
    if x>=N:
        ans+=1
    else:
        a[x]+=1
for i in range(1,N):
    if a[i]<i:
        ans+=a[i]
    else:
        ans+=a[i]-i
print(ans)


