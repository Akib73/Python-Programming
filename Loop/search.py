l1=(1,4,9,16,25,36,49,64,81,100)
s=len(l1)

a=int (input("Enter Numbrer:"))
count=0
flag=0
while count<s:
    if l1[count]==a:
        flag=1
        break
    count=count+1 
if flag==1:
    print("Number is found")

else :
    print("Number is not found")