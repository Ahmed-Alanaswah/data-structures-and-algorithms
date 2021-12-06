def Mergesort(arr):
    n = len(arr)

    if n > 1:
        mid = n//2
        left = []
        right =[]
        for i in range(mid):
            left.append(arr[i])
        for j in range(mid,n):  
            right.append(arr[j])
        
    
        for i in range(len(left)):
            for j in range(i+1,len(left)):
             if left[j]< left[i]:
                left[i],left[j] = left[j],left[i]


        for i in range(len(right)):
          for j in range(i+1,len(right)):
            if right[j]< right[i]:
              right[i],right[j]=right[j],right[i]
      
        Merge(left, right, arr)
        return arr 
      
def Merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1

        k = k + 1
        
    while i < len(left):
       arr[k]=left[i]
       i = i+1
       k = k+1
    while j < len(right):
       arr[k]=right[j]
       j = j+1
       k = k+1

     
   
    
     
       
print(Mergesort([2,3,5,7,13,11]))