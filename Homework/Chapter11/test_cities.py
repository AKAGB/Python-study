import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        result = city_country('Santiago', 'Chile')
        self.assertEqual(result, 'Santiago, Chile')

    def test_city_country_population(self):
        result = city_country('Santiago', 'Chile', population=500000)
        self.assertEqual(result, 'Santiago, Chile - population 500000')

if __name__ == '__main__':
    unittest.main()