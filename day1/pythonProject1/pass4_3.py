m=int(input())
n=int(input())
for x in range (1,m//5+1):
    for y in range(1,m//3+1):
        z=n-x-y
        if(z>0 and 5*x+3*y+z/3==100):
            print(x,y,z)
