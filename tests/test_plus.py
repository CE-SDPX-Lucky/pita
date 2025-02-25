import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    def test_plus1(self):
        response = self.app.get('/pita/3/4/5')
        self.assertEqual(response.data.decode('utf-8'), 'Yes')

    def test_plus2(self):
        response = self.app.get('/pita/3/4/6')
        self.assertEqual(response.data.decode('utf-8'), 'No')

if __name__ == '__main__':
    unittest.main()
