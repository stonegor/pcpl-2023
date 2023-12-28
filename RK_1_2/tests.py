import unittest
from collections import Counter
import data
from main import (
    get_musicians_with_orchestras,
    get_orchestras_with_musicians_count,
    get_musicians_orhestras_by_ending_substring,
)


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_get_musicians_with_orchestras(self):
        want = [
            ("Anna Netrebko", "Bolshoi Theatre Orchestra"),
            ("Daniil Trifonov", "St. Petersburg Philharmonic Orchestra"),
            ("Denis Matsuev", "State Academic Symphony Orchestra of Russia"),
            ("Evgeny Kissin", "Bolshoi Theatre Orchestra"),
            ("Marina Abramova", "St. Petersburg Philharmonic Orchestra"),
            ("Maxim Vengerov", "Mariinsky Theatre Orchestra"),
            ("Natalia Gutman", "Novosibirsk Symphony Orchestra"),
            ("Vadim Repin", "Mariinsky Theatre Orchestra"),
            ("Valery Gergiev", "Mariinsky Theatre Orchestra"),
            ("Yuri Bashmet", "Moscow City Symphony - Russian Philharmonic"),
        ]
        actual = get_musicians_with_orchestras(data.orchestras, data.musicians)
        self.assertCountEqual(want, actual)

    def test_get_orchestras_with_musicians_count(self):
        want = [
            ("Mariinsky Theatre Orchestra", 3),
            ("St. Petersburg Philharmonic Orchestra", 2),
            ("Bolshoi Theatre Orchestra", 2),
            ("Moscow City Symphony - Russian Philharmonic", 1),
            ("State Academic Symphony Orchestra of Russia", 1),
            ("Novosibirsk Symphony Orchestra", 1),
        ]
        actual = get_orchestras_with_musicians_count(data.orchestras, data.musicians)
        self.assertCountEqual(want, actual)

    def test_get_musicians_orhestras_by_ending_substring(self):
        want = [
            (
                "Daniil Trifonov",
                ["Mariinsky Theatre Orchestra", "Novosibirsk Symphony Orchestra"],
            ),
            ("Maxim Vengerov", ["Novosibirsk Symphony Orchestra"]),
        ]
        actual = get_musicians_orhestras_by_ending_substring(
            orechestras=data.orchestras,
            musicians=data.musicians,
            musicians_orchestras=data.musicians_orchestras,
            substring="ov",
        )
        self.assertCountEqual(want, actual)


if __name__ == "__main__":
    unittest.main()
