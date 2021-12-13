#Variable dan Input
tahun = int(input("Masukkan tahun : "))

#Conditional dan Output
if tahun % 400 == 0 :
    print("Tahun kabisat")
elif tahun % 100 == 0 :           #Tidak usah pake "and" dan "!=", karena jika
    print("Bukan tahun kabisat")  #sudah else maka sudah pasti tidak habis 
elif tahun % 4 == 0 :             #dibagi 400 (Kondisi If sebelumnya !=)
    print("Tahun kabisat")
else :
    print("Bukan tahun kabisat")

'''
Muhammad Zidane Naufal Ramadhan (1102213103)
EL-45-08
'''
