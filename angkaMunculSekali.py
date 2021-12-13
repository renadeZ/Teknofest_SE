def cariSatu(a):
    b = []
    global n
    c = 0
    for i in range(0, n):
        if (a.count(a[i]) == 1):
            b.insert(c, a[i])
            c+=1
    return b

x = []
n = int(input("Jumlah angka : "))
#Main
for i in range(0, n):
    print(f"Angka ke-{i+1} :", end=" ")
    x.insert(i, int(input()))
y = cariSatu(x)

print("Angka berjumlah satu : ", y)

'''
Muhammad Zidane Naufal Ramadhan (1102213103)
EL-45-08
'''