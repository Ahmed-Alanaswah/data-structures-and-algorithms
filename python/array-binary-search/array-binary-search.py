arr = [1,2,3,4]

x= input()

def BinarySearch(array,item):
    for i in range(len(arr)):
        if str(arr[i]) == x:
            return i
            break
    else:
        return -1
print(BinarySearch(arr,x))

