import unittest
from unittest.mock import patch, Mock

from main import )
    greet_human,
)

class TestMainApp(unittest, TestCase):
    def test_isitcoldf_freezing(self) -> None:
        """Test is_it_cold_f for freezing"""
        self.assertTrue(is_it_cold_f(32))

    def test_isitcoldf_boiling(self) -> None:
        """Test is_it_cold_f for boiling"""
        self.assertFalse(is_it_cold_f(212))

    def test_isitcoldf_negative(self) -> None:
        """Test is_it_cold_f for neg temps"""
        self.assertTrue(is_it_cold_f(-40))

    def test_isitcoldf_thresh(self) -> None:
        """Test is_it_cold_f for threshold"""
        self.assertFalse(is_it_cold_f(68))

    def test_isitcoldf_above(self) -> None:
        """Test is_it_cold_f for above the threshold"""
        self.assertFalse(is_it_cold_f(70))

    def test_isitcoldf_below(self) -> None:
        """Test is_it_cold_f for below the threshold"""
        self.assertTrue(is_it_cold_f(67))


    @patch('builtins.input', side_effect=['alice'])
    @patch('builtins.print')
    def test_greethuman_alice(self, mock_print: Mock, _: Mock) -> None:
        """Test imputting alice to greet_human"""
        greet_human()
        expected_calls = [
            unittest.mock.call("hello alice!"),
        ]
        mock_print.assert_has_calls(expected_calls)

if __name__ == "__main__":
    unittest.main()