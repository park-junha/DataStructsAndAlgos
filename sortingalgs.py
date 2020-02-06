# Take Python array as input
def SelectionSort(arr):
    print(arr)
    size = len(arr)
    for pivot in range(size):
        print("Current pivot index:", pivot)
        minValue = arr[pivot]
        indexOfMin = pivot
        for cursor in range(pivot, size):
            print("Current cursor index:", cursor)
            if arr[cursor] < minValue:
                indexOfMin = cursor
                minValue = arr[cursor]
            print("Current swap index:", indexOfMin)
        arr[pivot], arr[indexOfMin] = arr[indexOfMin], arr[pivot]
        print(arr)
    return arr

# Take Python array as input
def InsertionSort(arr):
    print(arr)
    size = len(arr)
    for pivot in range(size):
        print("Current pivot index:", pivot)
        for cursor in range(0, pivot):
            print("Current swap index:", cursor)
            if arr[cursor] > arr[pivot]:
                temp = arr.pop(pivot)
                arr.insert(cursor, temp) 
                print("Swapping index", pivot, "and index", cursor)
                break
        print(arr)
    return arr
