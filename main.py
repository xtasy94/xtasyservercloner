mytitle = "xtasy server cloner - Developed by xtasy"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
client_id = 'Your Account ID'
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import platform
from serverclone import Clone

client = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}
      _                   
     | |                  
__  _| |_ __ _ ___ _   _  
\ \/ / __/ _` / __| | | | 
 >  <| || (_| \__ \ |_| | 
/_/\_\\__\__,_|___/\__, | 
                    __/ | 
                   |___/  
                                                                                          
                                                                                                    
{Style.RESET_ALL}
                                                            {Fore.MAGENTA}Developed by: notxtasy.{Style.RESET_ALL}
        """)
token = input(f'Enter your token:\n >')
guild_s = input('Enter guild id you want to copy:\n >')
guild = input('Enter guild id where you want to copy:\n >')
input_guild_id = guild_s  
output_guild_id = guild  
token = token  


print("  ")
print("  ")

@client.event
async def on_ready():
    extrem_map = {}
    print(f"Logged In as : {client.user}")
    print("Cloning Server")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await Clone.guild_edit(guild_to, guild_from)
    await Clone.roles_delete(guild_to)
    await Clone.channels_delete(guild_to)
    await Clone.roles_create(guild_to, guild_from)
    await Clone.categories_create(guild_to, guild_from)
    await Clone.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}

   ______  __                               __  
 .' ___  |[  |                             |  ] 
/ .'   \_| | |  .--.   _ .--.  .---.   .--.| |  
| |        | |/ .'`\ \[ `.-. |/ /__\\/ /'`\' |  
\ `.___.'\ | || \__. | | | | || \__.,| \__/  |  
 `.____ .'[___]'.__.' [___||__]'.__.' '.__.;__] 
                                                

    {Style.RESET_ALL}""")
    await asyncio.sleep(5)
    client.close()


client.run(token, bot=False)
