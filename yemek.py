
def Listele():
    with open("YemekListesi.txt", "r") as FILE:
        for YEMEK in FILE:
            print(YEMEK)


def YemekAd():
    Yemekad = input("Yemegin Adını Girin: ")
    with open("YemekListesi.txt", "a") as FILE:
        FILE.write(Yemekad + '\n')


def MalzemeAd():
    malzemeİsmi = input('Malzeme Adı Girin: ')
    with open("YemekListesi.txt", "a") as FILE:
        FILE.write(malzemeİsmi + '\n')
       





while True:
    yemekID = input('1- Yemekleri Listele \n 2- Yemek Ekleyin \n 3-Malzeme Girin  \n 4- Exit\n')

    if yemekID == '1':
        Listele()
    elif yemekID == '2':
        YemekAd()
    elif yemekID == '3':
        MalzemeAd()
    else:
        break

