def selection_sort(theList):
    for i in range(len(theList)):
        min = i
        for k in range(i+1, len(theList)):
            if theList[k] < theList[min]:
                tmp = theList[i]
                theList[i] = theList[k]
                theList[k] = tmp
                
    return theList