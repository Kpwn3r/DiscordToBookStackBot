import os
import requests
from dotenv import load_dotenv

load_dotenv()

BOOKSTACK_TOKEN_ID = os.getenv('BOOKSTACK_TOKEN_ID') # BookStack API token ID
BOOKSTACK_TOKEN_SECRET = os.getenv('BOOKSTACK_TOKEN_SECRET')  # BookStack API secret token
BOOKSTACK_URL = os.getenv('BOOKSTACK_URL')  # BookStack URL

headers = {
    'Authorization': f'Token {BOOKSTACK_TOKEN_ID}:{BOOKSTACK_TOKEN_SECRET}',
    'Content-Type': 'application/json',
}

# Fetch the list of books
response = requests.get(f'{BOOKSTACK_URL}/books', headers=headers)

if response.status_code == 200:
    books = response.json()['data']
    for book in books:
        print(f"Book: {book['name']} - ID: {book['id']}")
else:
    print(f"Failed to retrieve books: {response.text}")
