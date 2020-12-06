#insertion sort with iteration count

list_of_no=[]
sorted_list=[]
count=0
scount=0

no=int(input("Enter the no of values:"))
for i in range(0,no):
    count+=1
    x=int(input("Enter no:"))
    list_of_no.append(x)
n=len(list_of_no)

for i in range(1, n):
    count+=1 
    temp = list_of_no[i]
    j = i-1
    while j >=0 and temp < list_of_no[j] :
        count+=1 
        scount+=1
        list_of_no[j+1] = list_of_no[j] 
        j -= 1
    list_of_no[j+1] = temp

print("Iteration Count:",count)
print("No of times swapping happens:",scount)
print("Sorted:",list_of_no)
