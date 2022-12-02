print("===== Program Manipulasi String =====")
print("Pilihan menu: \n1. Hitung kata \n2. Ubah kata")
a = input("Pilihan anda:")
b = input("Masukan sebuah kalimat/kata:")

def hitung_kata():
   
        a1 = input("Masukan kata yang ingin diitung:")
        a2 = b.count(a1)
        print("terdapat sebanyak",a2, "kata", a1, "di dalam kalimat")

def ubah_kata():
        b1 = input("Masukan kata yang ingin diubah:")
        b2 = input("Masukan kata pengganti:")
        b3 = b.replace(b1, b2)
        print("String berhasil diubah menjadi ;", b3)

if a=="1":
    hitung_kata()

elif a=="2":
    ubah_kata()

else:
    print("Pilihan yang anda input tidak terdaftar di daftar pilihan")
    



        
