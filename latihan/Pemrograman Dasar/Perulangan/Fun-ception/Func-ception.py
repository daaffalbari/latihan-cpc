a,b,x,y = map(int, input().split())

while(x < y):
  print(x)
  x = a * x + b
  if x > y:
    break
  