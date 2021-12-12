import unittest

from Prostokat import Prostokat


class MyTestProstokat(unittest.TestCase):

    def test_dlugosc_x(self):
        p1 = Prostokat(0, 0, 10, 20)
        dlugosc_obliczona = p1.dlugosc_x
        dlugosc_oczekiwana = 10
        self.assertEqual(dlugosc_obliczona, dlugosc_oczekiwana)  # add assertion here

    def test_dlugosc_y(self):
        p1 = Prostokat(0, 0, 10, 20)
        dlugosc_obliczona = p1.dlugosc_y
        dlugosc_oczekiwana = 20
        self.assertEqual(dlugosc_obliczona, dlugosc_oczekiwana)

    def test_pole(self):
        p1 = Prostokat(0, 0, 10, 20)
        pole_obliczona = p1.pole
        pole_oczekiwana = 200
        self.assertEqual(pole_obliczona, pole_oczekiwana)

    def test_obwod(self):
        p1 = Prostokat(0, 0, 10, 20)
        obwod_obliczona = p1.obwod
        obwod_oczekiwana = 60
        self.assertEqual(obwod_obliczona, obwod_oczekiwana)

if __name__ == '__main__':
    unittest.main()
