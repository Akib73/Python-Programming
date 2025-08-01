n=int (input("Enter Number:"))
def factorial (d):
    f=1
    for e in range(1,d+1):
        f=f*e
    print ("Fsctorial of ",d,"is:",f)

factorial(5)