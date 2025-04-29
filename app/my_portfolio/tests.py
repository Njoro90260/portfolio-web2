from django.test import TestCase

# Create your tests here.
import json

with open('data_utf8.json', 'r', encoding='utf-8') as file:
    try:
        json.load(file)
        print("Valid Json!")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
