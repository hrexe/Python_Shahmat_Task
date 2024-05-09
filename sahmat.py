class SahmatOyuncusu:
    def __init__(self, ad, derece):
        self.ad = ad
        self.derece = derece

    def yaris_vaxtlari(self):
        print("Sahmat yarışları həftədə 3 dəfə kecirilir.")

    def gunluk_yaris_sayi(self):
        return 4

class AzerbaycanCempionu(SahmatOyuncusu):
    pass

class DunyaCempionu(SahmatOyuncusu):
    def yaris_vaxtlari(self):
        print("Dünya Çempionu olan " + self.ad + " üçün yarışma vaxtları fərqlidir. Ətraflı məlumat üçün federasiyaya müraciət edin.")

def yaris_vaxti(oyuncu):
    oyuncu.yaris_vaxtlari()

azerbaycan_cempionu = AzerbaycanCempionu("Coders Azerbaijan Team", 1)
dunya_cempionu = DunyaCempionu("Coders Nakhchivan", 1)

print("Azərbaycan Çempionu:")
print("Ad:", azerbaycan_cempionu.ad)
print("Dərəcə:", azerbaycan_cempionu.derece)
print("Günlük Yarış Sayı:", azerbaycan_cempionu.gunluk_yaris_sayi())
yaris_vaxti(azerbaycan_cempionu)

print("\nDünya Çempionu:")
print("Ad:", dunya_cempionu.ad)
print("Dərəcə:", dunya_cempionu.derece)
print("Günlük Yarış Sayısı:", dunya_cempionu.gunluk_yaris_sayi())
yaris_vaxti(dunya_cempionu)
