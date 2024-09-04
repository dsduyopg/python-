money=float(input())
year=int(input())
rate=float(input())
F=money*(1+rate)**year
print("利息={:.2f}".format(F-money))