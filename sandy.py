s=int(input(""))

if(s>0):
    sum=0
    for i in range(1,s+1):
        if(i%2!=0):
            sum+=i
    print(sum)
else:
    print("Invalid Number")
            
