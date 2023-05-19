#BİL 104 ÖDEV-4
class Magaza:
    #boş dictionary'ler
    magazalar = {}
    saticilar = {}
    #mağazanın değişkenlerini atayan initilizar metodu
    def __init__(self, magaza_adi, satici_adi, satici_cinsi, satis_tutari):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__satis_tutari = satis_tutari
    #private değişkenleri class dışı döndüren fonksiyonlar
    def get_magaza_adi(self):
        return self.__magaza_adi
    
    def get_satici_adi(self):
        return self.__satici_adi
    
    def get_satici_cinsi(self):
        return self.__satici_cinsi
    
    def get_satis_tutari(self):
        return self.__satis_tutari
    #mağaza ve saticilara özel tutarları oluşturan fonksiyon
    def magaza_satis_tutar(self,dict):
        for magaza in dict:
            if magaza.get_magaza_adi() in self.magazalar:
                self.magazalar[magaza.get_magaza_adi()] += magaza.get_satis_tutari()
            else:
                self.magazalar[magaza.get_magaza_adi()] = magaza.get_satis_tutari()
            satici = magaza.get_satici_adi(), magaza.get_satici_cinsi()
            if satici in self.saticilar:
                self.saticilar[satici] += magaza.get_satis_tutari()
            else:
                self.saticilar[magaza.get_satici_adi(), magaza.get_satici_cinsi()] = magaza.get_satis_tutari()
    #tutarları ekrana yazan fonksiyon
    def __str__(self):
        print("\n\n**magazalar**")
        for magaza in self.magazalar:
            print("\n" + str(magaza) + ": " + str(self.magazalar[magaza]))
        print("\n**saticilar**")
        for satici in self.saticilar:
            print("\n" + str(satici) + ": " + str(self.saticilar[satici]) + "\n")

        
#main fonksiyon
def main():
    #boş dictionary ve devam değişkeni
    dict = {}
    devam = 'e'
    #magaza objesi oluşturup bu objeyi key değeri tutarı da value değeri olarak giren döngü
    while devam.lower()=='e':
        magaza = Magaza(input("\nMagaza adi: "), input("Satici adi: "),input("Satici cinsi: "), int(input("Satis tutari: ")))
        dict[magaza] = magaza.get_satis_tutari()
        devam = input("\ndevam?(e/h): ")
    #magaza satış tutarını bulan fonksiyonu ve ekrana tutarları yazan fonksiyonu çağırmak
    magaza.magaza_satis_tutar(dict)
    magaza.__str__()
#main fonksiyonunu 
if __name__ == main:
    main()
    