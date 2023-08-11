import unittest
from unittest.mock import patch
import lotto_generator 

class TestLottoNumberGeneratorApp(unittest.TestCase):

    @patch("builtins.input", side_effect=[""])
    def test_generate_lotto_draw(self, mock_input):
        lotto_draw = lotto_generator.generate_lotto_draw()
        self.assertEqual(len(lotto_draw), 6)
        self.assertTrue(all(1 <= num <= 50 for num in lotto_draw))

if __name__ == "__main__":
    unittest.main()

