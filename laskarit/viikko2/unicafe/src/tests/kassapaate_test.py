import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
       

    def test_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisia_lounaita_myyty_oikea_maara(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaita_lounaita_myyty_oikea_maara(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassassa_oleva_rahamaara_kasvaa_oikein_edullinen_lounas(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kassassa_oleva_rahamaara_kasvaa_oikein_maukas_lounas(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_vaihtorahan_suuruus_oikea_edullinen(self):
        #self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_vaihtorahan_suuruus_oikea_maukas(self):
        
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(550), 150)

    def test_edullisten_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaiden_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kassassa_oleva_rahamaara_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_oleva_rahamaara_ei_muutu_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_liian_pieni_maksu_palautetaan_edullinen(self):
        
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_liian_pieni_maksu_palautetaan_maukas(self):
        
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_myytyjen_maara_ei_muutu_jos_maksu_palautetaan_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myytyjen_maara_ei_muutu_jos_maksu_palautetaan_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_korttiosto_toimii(self):
        
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo_euroina(), 7.60)

    def test_maukkaan_lounaan_korttiosto_toimii(self):
        
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo_euroina(), 6.00)

    def test_edullisen_lounaan_korttioston_palautusarvo_on_oikea(self):

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)

    def test_maukkaan_lounaan_korttioston_palautusarvo_on_oikea(self):

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)

    def test_edullisten_lounaiden_maara_kasvaa_kortilla_ostaessa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaiden_lounaiden_maara_kasvaa_kortilla_ostaessa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullisen_lounaan_korttiosto_toimii_jos_raha_ei_riita(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo_euroina(), 1.00)

    def test_maukkaan_lounaan_korttiosto_toimii_jos_raha_ei_riita(self):
        self.kortti = Maksukortti(300)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo_euroina(), 3.00)

    def test_edullisten_lounaiden_maara_ei_muutu_kortiostossa_jos_raha_ei_riita(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaiden_lounaiden_maara_ei_muutu_kortiostossa_jos_raha_ei_riita(self):
        self.kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_korttioston_palautusarvo_on_oikea_jos_raha_ei_riita(self):
        self.kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), False)

    def test_maukkaan_lounaan_korttioston_palautusarvo_on_oikea_jos_raha_ei_riita(self):
        self.kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), False)

    def test_kassassa_oleva_rahamaara_ei_muutu_korttiostosta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_saldo_kasvaa_kun_kortille_ladataan_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 102000)

    def test_kortin_saldo_kasvaa_kun_kortille_ladataan_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 2000)
        self.assertEqual(self.kortti.saldo_euroina(), 30.00)
    
    def test_kassan_saldo_ei_muutu_kun_kortille_ladataan_negatiivinen_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_saldo_ei_muutu_kun_kortille_ladataan_negatiivinen_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, -2000)
        self.assertEqual(self.kortti.saldo_euroina(), 10.00)

    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.00)