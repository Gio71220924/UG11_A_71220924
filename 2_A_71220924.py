a = input("Masukan kata:")
b = int(len(a))


def cetak_kata(a):
    if  b %2 == 0:
        aa = a[0:3]
        ab = a[-3]
        print("Huruf yang diambil pada kata", a, "adalah ", aa, "dan", ab)

    else:
        bagian = int((b-3)/2)
        b = a[bagian:-bagian]
        print("Huruf yang diambil pada kata", a, "adalah", b)
        return a
    


