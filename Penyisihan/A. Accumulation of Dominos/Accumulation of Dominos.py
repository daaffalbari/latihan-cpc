n,m = map(int,input().split())
ret=0

if(m == 1):
  ret = n - 1
else:
  ret = (m-1)*n

print(ret)