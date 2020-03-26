from unittest import TestCase
from lab2 import to_json


class Test(TestCase):
    def test_to_json(self):
        murakami = to_json.Book()
        murakami.author = "H. Murakami"
        murakami.name = "Killing comrade"
        murakami.pages = "143"
        self.assertEqual(to_json.to_json(murakami), '{"author": "H. Murakami", "name": "Killing comrade", "pages": 143}')

    def test_wrong_to_json(self):
        murakami = to_json.Book()
        murakami.author = "H. Murakami"
        murakami.name = "Killing comrade"
        murakami.pages = "143"
        self.assertNotEqual(to_json.to_json(murakami), '{"author": "H. Murakami", "name": "Killing comrade", "pages": "143"}')
