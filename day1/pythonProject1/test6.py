m=int(input())
n=int(input())
def lcm(m,n):
    while n!=0:
        temp=n
        n=m%n
        m=temp
    return m
lcm_result =lcm(m, n)
print(lcm_result, end='')