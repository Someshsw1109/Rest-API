import requests
import unittest
class TestRestApi(unittest.TestCase):
    address = "http://127.0.0.1:8081"
    def test_GET1(self):
        r = requests.get(self.address + "/cars")
        self.assertEqual(r.status_code, 200)
    def test_GET2(self):
        r = requests.get(self.address + "/car/2")
        self.assertEqual(r.status_code, 200)
    def test_GET3(self):
        r = requests.get(self.address)
        self.assertEqual(r.status_code, 400)
    def test_GET4(self):
        r = requests.get(self.address + "/carcar/23")
        self.assertEqual(r.status_code, 400)
    def test_GET5(self):
        r = requests.get(self.address + "/carca")
        self.assertEqual(r.status_code, 400)
    def test_GET6(self):
        r = requests.get(self.address + "/car/45")
        self.assertEqual(r.status_code, 404)
    def test_POST1(self):
        payload = {
            "id": "24",
            "make": "BMW",
            "model": "Z4",
            "year": 2005,
            "price": 9300
        }
        r = requests.post(self.address + "/cars", json=payload)
        self.assertEqual(r.status_code, 202)
    def test_POST2(self):
        payload = {
            "id": "222",
            "make": "Wolkswagen",
            "model": "Golf",
            "year": 2011,
            "price": 8600
        }
        r = requests.post(self.address, json=payload)
        self.assertEqual(r.status_code, 400)
    def test_POST3(self):
        payload = {
            "id": "222",
            "make": "Wolkswagen",
            "model": "Golf",
            "year": 2011,
            "price": 8600
        }
        r = requests.post(self.address + "/car", json=payload)
        self.assertEqual(r.status_code, 400)
    def test_POST4(self):
        payload = {
            "id": "25",
            "make": "Audi",
            "model": "A4",
            "price": 7900
        }
        r = requests.post(self.address + "/cars", json=payload)
        self.assertEqual(r.status_code, 422)
    def test_POST5(self):
        payload = {
            "id": "114",
            "make": "Mercedes",
            "model": "CLA",
            "year": 2014,
            "price": 34000
        }
        r = requests.post(self.address + "/cars", json=payload)
        self.assertEqual(r.status_code, 202)
        r = requests.post(self.address + "/cars", json=payload)
        self.assertEqual(r.status_code, 409)
    def test_POST6(self):
        r = requests.post(self.address + "/cars")
        self.assertEqual(r.status_code, 400)
    def test_PUT1(self):
        payload = {
            "make": "Nissan",
            "model": "Skyline",
            "year": 1999,
            "price": 2200
        }
        r = requests.put(self.address + "/car/1", json=payload)
        self.assertEqual(r.status_code, 202)
    def test_PUT2(self):
        payload = {
            "make": "Nissan",
            "model": "Skyline",
            "year": 1999,
            "price": 2200
        }
        r = requests.put(self.address + "/car/9001", json=payload)
        self.assertEqual(r.status_code, 404)
    def test_PUT3(self):
        r = requests.put(self.address + "/car/1")
        self.assertEqual(r.status_code, 400)
    def test_PUT4(self):
        payload = {
            "make": "Nissan",
            "model": "Skyline",
            "year": 1999,
            "price": 2200
        }
        r = requests.put(self.address + "/loremipsum/42", json=payload)
        self.assertEqual(r.status_code, 400)
    def test_DELETE1(self):
        r = requests.delete(self.address + "/car/3")
        self.assertEqual(r.status_code, 202)
    def test_DELETE2(self):
        r = requests.delete(self.address + "/car/9002")
        self.assertEqual(r.status_code, 404)
    def test_DELETE3(self):
        r = requests.delete(self.address + "/cars/42")
        self.assertEqual(r.status_code, 400)
    def test_DELETE4(self):
        r = requests.delete(self.address + "/car/")
        self.assertEqual(r.status_code, 400)
if __name__ == '__main__':
    unittest.main()