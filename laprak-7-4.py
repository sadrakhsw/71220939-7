sebuah_kalimat = input("Inputan pertama:")
minim = ""
max = ""
akhir = sebuah_kalimat.split()

for i in range(len(akhir)):
    if i == 0 :
        minim = akhir[i]
        max = akhir[i]
    else:
        if len(max) < len(akhir [i]):
            max = akhir [i]

        elif len (minim) > len(akhir [i]):
            minim = akhir[i]
        
print("terpendek: ", minim)

print("terpanjang: ", max)
