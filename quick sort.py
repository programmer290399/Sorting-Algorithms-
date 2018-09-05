def quick_sort(data):
    
    if len(data) <= 1:
        return data

    pivot = len(data)-1  # choose the last component as pivot
    i = -1
    for j in range(0, len(data)-1):
        if data[j] < data[pivot]:
            i += 1
            data[i], data[j] = data[j], data[i]  # swap
            
    data[pivot], data[i+1] = data[i+1], data[pivot]
    
    return quick_sort(data[:i+1]) + [data[i+1]] + quick_sort(data[i+2:])