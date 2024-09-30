# Discord Channel to BookStack Book Archival Tool/Bot

## Features
- Export channel history into HTML document
- Automatically upload exported file to BookStack page

## Commands

- !export : exports the channel history to HTML file, then uploads to BookStack

## Installation

1. Clone the repository:

2. Navigate to the project directory:
    
3. Install the required dependencies:
    
    pip install -r requirements.txt

### Dependencies

- `discord.py` (version 2.0.0)
- `discord` (version 2.3.2)
- `requests` (version 2.28.1)
- `python-dotenv` (version 1.0.0)

### .env file creation/setup:

- TOKEN = xxxxx # Discord Bot token
- USER_TOKEN = xxxxx  # Discord user token
- BOOKSTACK_TOKEN_ID = xxxxx # BookStack API token ID
- BOOKSTACK_TOKEN_SECRET = xxxxx  # BookStack API secret token
- BOOKSTACK_URL = https://YourBookstackWebsite.com/api  # BookStack URL
- BOOKSTACK_BOOK_ID = 00 # Book ID (Obtained by using bookstackIdRequest.py)


## Credits

- This project uses [DiscordChatExporter](https://github.com/Tyrrrz/DiscordChatExporter) by [Tyrrrz](https://github.com/Tyrrrz)