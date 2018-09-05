def insertionSortModified(arr):

    n = len(arr)

    for i in range(1,n):

        temp = arr[i]
 
        li = 0
        ls = i-1

        while li<=ls:

           m = (li+ls)/2

           if arr[m] > temp:
              ls = m - 1
           else:
              li = m + 1 

        for j in range(i-1,li-1,-1):
            arr[j+1] = arr[j]

        arr[li] = temp

    return arr
