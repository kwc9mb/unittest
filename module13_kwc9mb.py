import unittest
import re
from datetime import datetime

class TestStockVisualizerInputs(unittest.TestCase):

    def test_symbol(self):
        def is_valid_symbol(symbol):
            return symbol.isupper() and 1 <= len(symbol) <= 7 and symbol.isalpha()
        
        self.assertTrue(is_valid_symbol("AAPL"))
        self.assertFalse(is_valid_symbol("apple"))
        self.assertFalse(is_valid_symbol("AAPL123"))
        self.assertFalse(is_valid_symbol("A"))
    
    def test_chart_type(self):
        def is_valid_chart_type(chart_type):
            return chart_type in ["1", "2"]
        
        self.assertTrue(is_valid_chart_type("1"))
        self.assertTrue(is_valid_chart_type("2"))
        self.assertFalse(is_valid_chart_type("0"))
        self.assertFalse(is_valid_chart_type("3"))
        self.assertFalse(is_valid_chart_type("a"))

    def test_time_series(self):
        def is_valid_time_series(time_series):
            return time_series in ["1", "2", "3", "4"]
        
        self.assertTrue(is_valid_time_series("1"))
        self.assertTrue(is_valid_time_series("4"))
        self.assertFalse(is_valid_time_series("0"))
        self.assertFalse(is_valid_time_series("5"))
        self.assertFalse(is_valid_time_series("a"))

    def test_start_date(self):
        def is_valid_date(date_str):
            try:
                datetime.strptime(date_str, '%Y-%m-%d')
                return True
            except ValueError:
                return False

        self.assertTrue(is_valid_date("2023-01-01"))
        self.assertFalse(is_valid_date("01-01-2023"))
        self.assertFalse(is_valid_date("2023/01/01"))
        self.assertFalse(is_valid_date("2023-13-01"))

    def test_end_date(self):
        # Reusing the is_valid_date function from test_start_date
        self.assertTrue(is_valid_date("2023-12-31"))
        self.assertFalse(is_valid_date("31-12-2023"))
        self.assertFalse(is_valid_date("2023/12/31"))
        self.assertFalse(is_valid_date("2023-12-32"))

if __name__ == '__main__':
    unittest.main()