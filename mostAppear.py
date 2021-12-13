def singleSort(a, b):
    #Remove Duplicate
    storeItem = []
    storeCount = []
    x = sorted(item)
    storeItem.append(x[0])
    for i in range(1, n):
        if x[i] != x[i-1]:
            storeItem.append(x[i])

    #Count
    for i in range(0, len(storeItem)):
        text = storeItem[i]
        storeCount.append(item.count(storeItem[i]))

    #Sort
    Sorted = sorted(storeCount)
    counted = storeCount
    sortedIndex = []
    for i in range(0, len(Sorted)):
        for j in range(0, len(Sorted)):
            if Sorted[i] == counted[j]:
                sortedIndex.append(j)
                counted[j] = ""
                break

    #Output
    for i in range(0, len(storeItem)):
        print(f"{storeItem[sortedIndex[i]]} : {Sorted[i]}")
        
#Main
n = int(input("Masukkan jumlah item : "))
item = []
for i in range(0, n):
    print(f"Masukan item ke-{i+1} =", end=" ")
    item.append(input())
singleSort(item, n)

'''
Muhammad Zidane Naufal Ramadhan (1102213103)
EL-45-08
'''