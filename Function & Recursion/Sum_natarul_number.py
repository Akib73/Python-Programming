n=int (input("Enter Number:"))

def sumnumber(d):
    if (d==0):
        return 0
    return d + sumnumber(d-1)
a= sumnumber(n)
print(a)