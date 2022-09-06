# a grid N x M
# B, if the cell is black
# W, if the cell is white
# input format : N M

n,m=map(int,input().split())

for i in range(n):
    for j in range(m):
        if(i%2==0):
            if(j%2==1):
                print("B",end="")
            else:
                print("W",end="")
        else:
            if(j%2==0):
                print("W",end="")
            else:
                print("B",end="")
    print("")
