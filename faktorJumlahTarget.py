def cariPenjumlah(a, b):
    global n
    r = []
    c = 0
    for i in range(0, n-1):
        for j in range (i+1, n):
            if (a[i]+a[j]==b):
                r.append([a[i]])
                r[c].append(a[j])
                c +=1
    return r


x = []
n = int(input("Jumlah angka : "))
for i in range(0, n):
    print(f"Angka ke-{i+1} : ", end=" ")
    x.append(int(input()))
y = int(int(input("Cari penjumlah untuk angka : ")))
z = cariPenjumlah(x, y)

print(z)

'''
Muhammad Zidane Naufal Ramadhan (1102213103)
EL-45-08
'''