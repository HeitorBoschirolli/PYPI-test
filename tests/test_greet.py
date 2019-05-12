import unittest

from hellozawarudo import return_za_warudo, display_random_img

class TestZaWarudo(unittest.TestCase):

    def test_print(self):
        self.assertEqual(return_za_warudo(), 'ZA WARUDO')

    def test_display_random_img(self):
        display_random_img()

