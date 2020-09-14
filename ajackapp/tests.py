from django.test import TestCase
import requests

url = 'http://127.0.0.1:8000'
headers = {'Authorization': 'Token bc5478b3a61d41e6d1627bbd9c1bd24b076af228'}
r = requests.get(url, headers=headers)


# Create your tests here.
