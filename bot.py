import discord
import subprocess
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN') # Bot token
USER_TOKEN = os.getenv('USER_TOKEN')  # User token here
client = discord.Client(intents=discord.Intents.all())

BOOKSTACK_TOKEN_ID = os.getenv('BOOKSTACK_TOKEN_ID') # BookStack API token ID
BOOKSTACK_TOKEN_SECRET = os.getenv('BOOKSTACK_TOKEN_SECRET')  # BookStack API secret token
BOOKSTACK_URL = os.getenv('BOOKSTACK_URL')  # BookStack URL
BOOKSTACK_BOOK_ID = os.getenv('BOOKSTACK_BOOK_ID')


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the DiscordChatExporter executable
exporter_executable = os.path.join(script_dir, 'DiscordChatExporter.Cli.win-x64', 'DiscordChatExporter.Cli.exe')



def upload_to_bookstack(title, content):
    headers = {
        'Authorization': f'Token {BOOKSTACK_TOKEN_ID}:{BOOKSTACK_TOKEN_SECRET}',
        'Content-Type': 'application/json',
    }
    
    # Create a new page in BookStack
    data = {
        'name': title,
        'html': content,
        'book_id': BOOKSTACK_BOOK_ID,  
        'slug': title.replace(' ', '-').lower(),  # Create a slug from the title
    }
    
    response = requests.post(f'{BOOKSTACK_URL}/pages', headers=headers, json=data)
    return response



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!export'):
        # Specify the channel ID
        channel_id = message.channel.id
        
        # Build the export commands
        output_file = f'{channel_id}_history.html'
        export_command = [
            exporter_executable,
            'export',
            '--token', USER_TOKEN,
            '--channel', str(channel_id),
            '--output', output_file,
        ]

        # Run the command
        result = subprocess.run(export_command, capture_output=True, text=True)

        if result.returncode == 0:
            await message.channel.send("Chat history exported successfully.")
            await message.channel.send(file=discord.File(output_file))
            
        else:
            # Send the error message in chunks
            error_message = result.stderr
            for i in range(0, len(error_message), 2000):  # Split into chunks of 2000 characters
                await message.channel.send(f"Error exporting chat: {error_message[i:i+2000]}")
       
       
        
        # Read the HTML content
        with open(output_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Upload to BookStack
        response = upload_to_bookstack(f'Channel History - {channel_id}', html_content)
        if response.status_code == 201:
            await message.channel.send("Successfully uploaded to BookStack!")
        else:
            await message.channel.send(f"Failed to upload to BookStack: {response.text}")
        
        
            
client.run(TOKEN)
