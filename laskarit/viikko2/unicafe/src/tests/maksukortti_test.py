import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_saldo_vahenee_oikein_jos_rahaa_on(self):
        self.maksukortti.ota_rahaa(400)
        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_ota_rahaa_metodin_palautusarvo(self):
        #self.maksukortti.ota_rahaa(400)
        self.assertEqual(self.maksukortti.ota_rahaa(400), True)

    def test_ota_rahaa_metodin_palautusarvo_jos_raha_ei_riita(self):
        #self.maksukortti.ota_rahaa(1500)
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)

    def test_saldo_euroissa(self):
        self.assertEqual(self.maksukortti.__str__(), "Kortilla on rahaa 10.00 euroa")