import unittest
from city_functions import get_city_details

class TestCities(unittest.TestCase):
    """Test city_functions.py"""
    def test_city(self):
        """Do details like Sydney, Australia pass the test?"""
        city = get_city_details('sydney', 'australia')
        self.assertEqual(city, 'Sydney, Australia')

    def test_city_population(self):
        """Do details like Sydney, 25000000, Australia pass the test?"""
        city = get_city_details('sydney', 'australia', '25000000')
        self.assertEqual(city,'Sydney, 25000000, Australia')


if __name__ == '__main__':
    unittest.main()