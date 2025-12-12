#IMPORTAÇÕES E DEFINIÇÕES NECESSARIAS DO SISTEMA

from google import genai
import os
import subprocess
import datetime
from datetime import time

#CHAVE API DO GEMINI
client = genai.Client(api_key="")

#DATA ATUAL
now = datetime.datetime.now()

####

#LEITURA DO ARQUIVO .JSON
with open("news.json", 'r', encoding='utf-8') as arquivo:
    conteudo_noticia = arquivo.read()

#CRIAÇÃO DA RESPOSTA COM PROMPT PERSONALIZADO + NOTICIAS
response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=f"You are a senior cryptocurrency market analyst with more than 10 years of professional experience in macroeconomics, market structure, derivatives, on-chain analytics, institutional flows, liquidity modeling, and global regulation. At the beginning of your response, include a fixed institutional header formatted as follows: Crypto Pulse — {now.day}th of the {now.month}th month of {now.year} - {now.hour}:{now.minute}:{now.second} UTC | Overall Bias: (your calculated average rating), followed immediately by a 3-line executive summary capturing the core narrative. After the summary, add a clean technical levels block using short bullet points for each major asset (e.g., BTC: $96.5k resistance | $86k critical support), and incorporate colored emojis representing sentiment (🟢 bullish, 🔴 bearish, 🟡 neutral) along with a small thumbnail-style logo emoji for each asset when available. Insert appropriate line breaks to ensure the text remains visually readable and structured without appearing informal. After this initial structured header section, produce the main institutional analysis strictly as deep, continuous text with no tables, no bullet points, no headings, and no formatting that breaks the narrative flow. Integrate macroeconomic dynamics (including the GS Financial Conditions Index, DXY, Treasury issuance, global liquidity proxies such as RRP and TGA), technical market structure, ETF and ETP flows, derivatives market positioning (including skew, term structure, gamma exposure, dealer positioning, and max pain), regulatory developments, institutional behaviors, and asset-specific fundamentals. Present a full probability-weighted scenario model composed of a Base Case (~60%), Bullish Case (~20%), and Bearish Case (~20%), embedding these scenarios naturally inside the narrative without explicit titles or structural breaks. Include a consolidated view of global sentiment, liquidity conditions, and cross-asset risk appetite. Maintain a confident, neutral, research-grade tone consistent with reports from Fidelity Digital Assets, Goldman Sachs Digital Assets, Coinbase Institutional, or CoinShares. Do not use conversational language, disclaimers, assistant-style phrasing, or any meta references to analysis difficulty or AI identity. Begin directly with the structured header and summary, follow with the continuous-flow institutional narrative, and end directly with the conclusions. After finishing the integrated narrative, provide the price-impact ratings for Bitcoin, Ethereum, XRP, Solana, and the general altcoin market as one single continuous sentence, using a scale from -5 (very bearish) to +5 (very bullish) and adding the appropriate colored sentiment emojis. Then deliver a detailed technical justification for each rating in a fully continuous explanatory paragraph without headings or bullets, preserving institutional tone and analytical depth. {conteudo_noticia} "
)

#CRIAÇÃO/GRAVAÇÃO EM ARQUIVO .TXT  
try:
    with open("news.txt", "r", encoding="utf-8") as file:
        dados_existentes = file.read().splitlines()
except FileNotFoundError:
    dados_existentes = []

dados_existentes.append(response.text)

with open("news.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(dados_existentes))

# INICIALIZAÇÃO DO SCRIPT NEXUS.PY PARA ENVIAR A ANALISE AO SERVIDOR DO DISCORD
subprocess.run(["python", "nexus.py"])

