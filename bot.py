#IMPORTAÇÕES E DEFINIÇÕES NECESSARIAS DO SISTEMA

import discord
from discord.ext import commands, tasks
import datetime
from datetime import time
import subprocess

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

####

#EVENTO DE DEFINIÇÃO DE AÇÃO NA INICILIZAÇÃO DO BOT
@bot.event
async def on_ready():                                                                                 
    print("Aethos inicializado com sucesso")
    subprocess.run(["python", "coindesk.py"])
    verify_hour.start() #INICIALIZAÇÃO DA CONTAGEM DE TEMPO PARA AÇÃO

#EVENTO DE MENSAGEM BOAS VINDAS PARA O USUARIO
@bot.event
async def on_member_join(membro:discord.Member):
    canal = bot.get_channel() #ID DO CANAL ESPECIFICO PARA ESSA MENSAGEM
    await canal.send(f"Hello, {membro.mention}! Welcome to the server!")

#INICIALIZAÇÃO DO PROCESSO DE CAPTURA DE DADOS E ENVIO DE ANALISES A CADA DETERMINADO TEMPO
@tasks.loop(hours=24)
async def verify_hour():
    print("Verify Hour Start")
    now = datetime.datetime.now()
    if(now.minute == 59): 
        subprocess.run(["python", "coindesk.py"])  
         
#CHAVE API DO BOT
bot.run("")