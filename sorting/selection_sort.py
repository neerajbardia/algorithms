#selection sort with iteration count

list_of_no=[]
count=0
scount=0

no=int(input("Enter the no of values:"))
for i in range(0,no):
    count+=1
    x=int(input("Enter no:"))
    list_of_no.append(x)
n=len(list_of_no)

for i in range(0,n):
    count+=1
    min=list_of_no[i]
    for j in range(i+1,n):
        count+=1
        if min>list_of_no[j]:
            count+=1
            min=list_of_no[j]
            scount+=1
            list_of_no[i],list_of_no[j]=list_of_no[j],list_of_no[i]


print("Iteration Count:",count)
print("No of times swapping happens:",scount)
print("Sorted:",list_of_no)
