# binary search with comparison count

list_of_no=[]
flag=0
comparison_count=0
def binary_search(list_of_no, x): 
    min = 0
    max = len(list_of_no) - 1
    mid = 0
    global comparison_count
    while min <= max: 
        mid = (max + min) // 2
        comparison_count+=1
        if list_of_no[mid] < x: 
            min = mid + 1
        elif list_of_no[mid] > x: 
            max = mid - 1
        else: 
            return mid 
    return -1

print("-----------Binary Search----------")
no=int(input("Enter the no of values:"))
for i in range(0,no):
    x=int(input("Enter no:"))
    list_of_no.append(x)
search=int(input("Enter the no to search:"))
result = binary_search(list_of_no, search) 

if result != -1: 
	print("Element is present at index", str(result)) 
else: 
	print("Element is not present in array") 

print("Comparison Count:",comparison_count)
