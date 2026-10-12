#program to update the value of an element at a given index
arr=[]
num=int(input("Enter the no. of element of Array:"))

for i in range(num):
    element=int(input("Enter the element of array:"))
    arr.append(element)

index=int(input("Enter the postion of element"))
new_value=int(input("Enter the new value to update array:"))

print("Array before Updation",arr)
arr[index]=new_value
print("Array After updation",arr)
