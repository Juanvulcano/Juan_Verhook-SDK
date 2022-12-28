import requests
import unittest


class TestAPIMethods(unittest.TestCase):
    def test_get_api_check_status_code_equals_200(self):
        response = requests.get("https://the-one-api.dev/v2/book/")
        self.assertEqual(response.status_code, 200)

    def test_get_api_check_content_type_equals_json(self):
        response = requests.get("https://the-one-api.dev/v2/book/")
        self.assertEqual(response.headers["Content-Type"], "application/json; charset=utf-8")

    def test_get_api_check_known_book_exists(self):
        response = requests.get("https://the-one-api.dev/v2/book/")
        serialized_response = response.json()
        all_books = " ".join([book['name'] for book in serialized_response['docs']])
        self.assertIn("The Return Of The King", all_books) 

if __name__ == '__main__':
    unittest.main()