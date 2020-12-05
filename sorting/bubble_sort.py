# bubble sort with iteration count
list_of_no=[]
count=0
scount=0
no=int(input("Enter the no of values:"))
for i in range(0,no):
    count+=1
    x=int(input("Enter no:"))
    list_of_no.append(x)
n=len(list_of_no)
for i in range(0,n-1):
    count+=1
    for j in range(0,n-i-1):
        count+=1
        if list_of_no[j]>list_of_no[j+1]:
            count+=1
            scount+=1
            list_of_no[j],list_of_no[j+1]=list_of_no[j+1],list_of_no[j]
    
print("Iteration Count:",count)
print("No of times swapping happens:",scount)
print("Sorted:",list_of_no)
