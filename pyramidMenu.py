#Pilihan menu
print(
'''
Pilih Bentuk
1. Half Pyramid Pattern
2. Inverted Half Pyramid Pattern
3. Half Pyramid Pattern Mirrored
4. Full Pyramid Pattern
5. Full Pyramid Pattern Mirrored
'''
)

#Variables dan Input
menu = int(input("Pilihan : "))
if menu < 1 or menu > 5 :
    print("Pilihan tidak valid")
else :
    n = int(input("Jumlah bintang maksimal : "))

#Proses Conditional:
    #1. Half Pyramid Pattern
if menu == 1 :
    for i in range(0, n) :
        for j in range(0, i+1) :
            print("*", end=" ")
        print()

    #2. Inverted Half Pyramid Pattern
elif menu == 2 :
    for i in range(0, n) :
        for j in range(n-i, 0, -1) :
            print("*", end=" ")
        print()

    #3. Half Pyramid Pattern Mirrored
elif menu == 3 :
    for i in range(0, n) :
        for j in range(0, n-(i+1)) :
            print(end="  ")
        for j in range(0, i+1) :
            print("*", end=" ")
        print()

    #4. Full Pyramid Pattern
elif menu == 4 :
    for i in range(0, n) :
        for j in range(0, n-(i+1)) :
            print(end=" ")
        for j in range(0, i+1) :
            print("*", end=" ")
        print()

    #5. Full Pyramid Pattern Mirrored
elif menu == 5 :
    for i in range(0, n) :
        for j in range(0, i+1) :
            print(end=" ")
        for j in range(n-i, 0, -1) :
            print("*", end=" ")
        print()

'''
Muhammad Zidane Naufal Ramadhan (1102213103)
EL-45-08
'''