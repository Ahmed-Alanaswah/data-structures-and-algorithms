def SelectionSort(arr):
    n = len(arr)
    for i in range(n) :
        min = i
        for j in range(i+1, n):
            if (arr[j] < arr[min]):
                min = j
                print(min)

        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
        
    return arr  
        
print(SelectionSort([2,3,5,7,13,11]))