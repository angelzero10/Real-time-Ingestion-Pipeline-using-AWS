import unittest
from src.app import read_csv, add_timestamp

class TestApp(unittest.TestCase):
    def test_read_csv(self):
        rows = read_csv('data/recommended-fishing-rivers-and-streams-1.csv')
        self.assertIsInstance(rows, list)
        self.assertGreater(len(rows), 0)

    def test_add_timestamp(self):
        row = {'SampleKey': 'SampleValue'}
        row_with_timestamp = add_timestamp(row.copy())
        self.assertIn('Timestamp', row_with_timestamp)
        self.assertEqual(row['SampleKey'], row_with_timestamp['SampleKey'])

if __name__ == '__main__':
    unittest.main()
