import os
import sys
import unittest
import argparse

from rungen import rungen_urls

OONI_FOUR = """https://run.ooni.io/nettest?tn=web_connectivity&ta=%7B%22urls%22%3A%5B%22https%3A%2F%2Fwikipedia.org%22%2C%22https%3A%2F%2Fen.wikipedia.org%22%2C%22https%3A%2F%2Fes.wikipedia.org%22%2C%22https%3A%2F%2Ftwitter.com%22%2C%22https%3A%2F%2Fwhatsapp.com%22%5D%7D&mv=1.2.0"""
OONI_TWO = """https://run.ooni.io/nettest?tn=web_connectivity&ta=%7B%22urls%22%3A%5B%22https%3A%2F%2Ffacebook.com%22%2C%22https%3A%2F%2Fwww.nytimes.com%2F2019%2F04%2F10%2Fopinion%2Finternet-privacy-resources.html%22%5D%7D&mv=1.2.0"""


class TestRunGen(unittest.TestCase):
    def setUp(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--file")
        self.parser.add_argument("--list")
        self.parser.add_argument("--prefix", default=True)

    def test_foururls(self):
        os.chdir("tests")
        output = rungen_urls(self.parser.parse_args(["--file", "four-urls.txt"]))
        self.assertEqual(output, OONI_FOUR)

    def test_twourls(self):
        output = rungen_urls(self.parser.parse_args(["--file", "two-urls.txt"]))
        self.assertEqual(output, OONI_TWO)


if __name__ == "__main__":
    unittest.main()
