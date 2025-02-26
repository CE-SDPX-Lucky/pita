import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_x_is_1(self):
        response = self.app.get('/cir_round/1')
        self.assertEqual(response.data.decode('utf-8'), '6.28')

    def test_x_is_neg10(self):
        response = self.app.get('/cir_round/-10')
        self.assertEqual(response.data.decode('utf-8'), '0.00')

    def test_x_is_1dot5(self):
        response = self.app.get('/cir_round/1.5')
        self.assertEqual(response.data.decode('utf-8'), '9.42')

if __name__ == '__main__':
    unittest.main()
