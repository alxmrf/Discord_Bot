import discord as ds
from discord.flags import Intents
from discord.webhook import async_
from discord.ext import commands
from dotenv import load_dotenv
import os

class bot():
    
    
    #BOT constructor
    def __init__(self):
        self.Bot_intents = ds.Intents.all()    #sets up bot intents  for information on intents check the discord documentation #intents set to all
        self.Bot = commands.Bot(command_prefix = "!", intents = self.Bot_intents)    #creates an instance of the bot client using the discord.ext framework check discord.py documentation 
        self.token = self.load_token() #MUDAR DEPOIS EXTREMAMENTE ERRADO FAZER SEM .ENV
        
        @self.Bot.event
        async def on_ready():
            print("connected")
    
    #initializes the connection to discord
    
    def load_token(self):
        load_dotenv()
        return os.getenv("TOKEN")
    
    def connect_to_discord(self):
        self.Bot.run(self.token)
        

