#linear searching techniques

list_of_no=[]
flag=0
count=0
comparison_count=0
print("-----------Linear Search----------")
no=int(input("Enter the no of values:"))
for i in range(0,no):
    count+=1
    x=int(input("Enter no:"))
    list_of_no.append(x)
n=len(list_of_no)
search=int(input("Enter no to be searched:"))
for i in range(0,n): 
    comparison_count+=1  
    if list_of_no[i]==search:
        print("Element found at position ",i+1)
        flag=1
        break
if flag==0:
    print("Element not found in list!")

print("Comparison Count:",comparison_count)
