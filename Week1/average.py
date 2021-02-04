n=int(input("Amount of temperatures to be inserted: "))
a=[]
for i in range(0,n):
    num=int(input("Enter temperature: "))
    a.append(num)
avg=sum(a)/n
print("Average of temperatures:",round(avg,2))
