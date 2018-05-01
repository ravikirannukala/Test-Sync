import unittest
import index
import json


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        result = index.handler(None, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('{"records": [{"id": "Org1", "name": "Test Org 1"}, {"id": "Org2", "name": "Test Org 2"}, {"id": "Org3", "name": "Test Org 3"}]}', result['body'])


if __name__ == '__main__':
    unittest.main()
