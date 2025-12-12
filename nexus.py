#IMPORTAÇÕES E DEFINIÇÕES NECESSARIAS DO SISTEMA

import discord
from discord.ext import commands
import subprocess
import os

#DEVIDO AO LIMITE DE TAMANHO DE MENSAGEM DO DISCORD É NECESSARIO A SEPARAÇÃO DO CONTEUDO EM BLOCOS
def dividir_mensagem(texto, limite=2000):
    return [texto[i:i+limite] for i in range(0, len(texto), limite)]

#VARIAVEIS DE CONFIGURAÇÃO DE EVENTOS DO BOT
intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)

#LEITURA DO ARQUIVO NEWS.TXT
with open("news.txt", 'r', encoding='utf-8') as arquivo:
    conteudo_noticia = arquivo.read()

#EVENTO DE INICIALIZAÇÃO DO BOT SEGUIDO DO ENVIO DA NOTICIA, APAGAMENTO DOS ARQUIVOS .JSON E .TXT E DESLIGAMENTO DO BOT
@bot.event
async def on_ready():
    print("Nexus inicializado com sucesso")
    canal = bot.get_channel() #ID DO CANAL DESEJADO QUE A MENSAGEM SEJA ENVIADA

    partes = dividir_mensagem(conteudo_noticia)

    for parte in partes:
        await canal.send(parte)

    os.remove("news.txt")
    os.remove("news.json")

    await bot.close()

#CHAVE API DO BOT
bot.run("")
