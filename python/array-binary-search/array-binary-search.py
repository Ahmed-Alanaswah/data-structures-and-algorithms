arr=[1,2,4,5,6,7,9,10]

low = 0 
high= len(arr)
num = int(input())
def binarySearch(arr,low,high,num):
  if low > high :
    return -1
  if num > arr[-1]:
    return -1
  mid =  (low + high)//2 
  for  i in range(len(arr)):
    if num == arr[mid]:
      return mid
      break

    elif num > arr[mid]:
      low = mid +1 
      return binarySearch(arr,low,high,num)
      break
    elif num < arr[mid]:
      high = mid-1 
      return binarySearch(arr,low ,high,num)
      break
     
print(binarySearch(arr,low,high,num))

  
  
