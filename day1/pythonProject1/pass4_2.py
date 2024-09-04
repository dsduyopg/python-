n=int(input())
sum=0
flag=1
for i in range(1,2*n,2):
    sum+=(1/i)*flag
    flag*=-1
print(sum)
print(sum * 4)