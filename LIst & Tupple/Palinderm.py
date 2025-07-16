l=[]
l.append(input(" Enter 1st number:"))
l.append(input("Enter 2nd Number:"))
l.append(input("Enter 3rd Numer:"))
copy_l=l.copy()
copy_l.reverse()
if (l==copy_l):
    print("It is a palindrom")
else:
    print("It is not Palindrom ")