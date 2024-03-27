

class Personel:
    def __init__(self, ad_soyad, departman, calisma_yili, maas):
        self.ad_soyad=ad_soyad
        self.departman=departman
        self.calisma_yili=calisma_yili
        self.maas=maas

class Firma:
    personel_listesi=[]
    
    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)
    
    def personel_listele(self):
        i=1
        for p in self.personel_listesi:
            print("{}. {} : departman = {}, calisma yili={}, maas={}".format(i, p.ad_soyad, p.departman,p.calisma_yili, p.maas))
            i=i+1
            
    def maas_zammi(self, personel, zam_orani):
        personel.maas=personel.maas+(personel.maas*zam_orani)/100
        
    def personel_cikart(self, personel):
        for p in self.personel_listesi:
            if p.ad_soyad==personel.ad_soyad:
                self.personel_listesi.remove(p)
        
        
        
personel1 = Personel("Ayse_Soydan", "Insan Kaynaklari", 2024, 1000)
personel2 = Personel("Yusuf_Yilmaz", "Pazarlama", 2021, 6000)
personel3 = Personel("Elmas_Ozdemir", "Istatistik", 2018, 9000)


        
firma1=Firma()

firma1.personel_ekle(personel1)
firma1.personel_ekle(personel2)
firma1.personel_ekle(personel3)


firma1.personel_listele()

print(personel1.maas)
firma1.maas_zammi(personel1, 20)
print(personel1.maas)

firma1.personel_cikart(personel1)

firma1.personel_listele()














        

