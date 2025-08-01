l=[1,2,3,4,5]
def print_list (d,i=0):
    if (i==len(d)):
       return
    print (d[i])
    print_list (d,i+1)

print_list(l,0)