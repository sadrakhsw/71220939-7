def anagram(x,y):
    if sorted(x) == sorted(y):
        print(True)
    else :
        print(False)

kata_1 = input("kata 1 : ")
kata_2 = input("kata 2 : ")

anagram(kata_1,kata_2)
