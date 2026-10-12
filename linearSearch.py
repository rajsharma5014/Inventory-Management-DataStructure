#program to search for a given element in an array using Linear Search
arr=[]
num=int(input("Enter the no. of element of Array:"))

for i in range(num):
    element=int(input("Enter the element of array:"))
    arr.append(element)

found=False
search=int(input("Enter the element to find in aray:"))

for i in range(num):
    if arr[i]==search:
        print(search,"Element found in array at index",i)
        found=True
        break
if found==False:
    print("Element Not found in Array")
