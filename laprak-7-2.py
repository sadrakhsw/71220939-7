string_1 = input("Masukkan kalimat: ")
string_2 = input("Masukkan kata yang ingin dicek: ")
string_1_nochar = string_1.replace("."," ")

string_1_upper = string_1_nochar.upper()
string_2_upper = string_2.upper()

string_1_split = string_1_upper.split()
count = 0
for x in string_1_split:
    if string_2_upper == x:
        count += 1
    else:
        continue

print("%s ada %d buah"%(string_2,count))
