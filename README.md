Crypto News Radar

Este é um sistema automatizado e modular de análise de mercado financeiro, projetado para realizar web scraping de notícias, gerar relatórios institucionais aprofundados sobre criptomoedas utilizando o modelo Gemini da Google, e publicar o resultado final em um canal do Discord. 
O projeto opera de forma autônoma, garantindo que análises de alto nível sejam entregues de forma pontual e consistente.

🚀 Funcionalidades Principais:

  📰 Web Scraping Orientado: Captura artigos de notícias e dados do mercado de fontes como CoinDesk e CoinTelegraph.
  🤖 Geração de Análise Institucional (Gemini): Utiliza a API do Google Gemini para processar as notícias e gerar relatórios completos, com foco em macroeconomia, liquidez, análise on-chain e estrutura de mercado.
  📐 Formato de Relatório Estruturado: O relatório gerado adere a um formato rigoroso, incluindo um Institutional Header, Executive Summary, Technical Levels e uma narrativa contínua com cenários de probabilidade ponderada (Base, Bullish, Bearish).
  ⏱️ Automação Completa (Discord Bots): Dois bots de Discord (Aethos e Nexus) gerenciam o ciclo completo, desde o início do scraping agendado (a cada 24 horas) até a publicação final da análise no canal desejado.
  🧹 Limpeza Automática: Após a publicação, os arquivos temporários de dados (news.json e news.txt) são automaticamente deletados para manter o sistema limpo.
  ⚙️ Arquitetura do Sistema: O fluxo de trabalho é orquestrado por múltiplos scripts Python, cada um com uma função específica: 
    bot.py (Aethos): O bot principal de agendamento. Inicializa o processo de scraping e executa o ciclo a cada 24 horas usando @tasks.loop. 
    coindesk.py & coinint.py: Módulos de Web Scraping. Coletam dados de notícias de diversas URLs de ativos (BTC, ETH, XRP, SOL) e outras fontes, salvando o conteúdo bruto no arquivo news.json.
    gemini.py: O núcleo de inteligência. Lê o news.json, envia o conteúdo junto com um prompt detalhado e institucional para o modelo Gemini, e salva a análise gerada em news.txt.
    nexus.py (Nexus): O bot de publicação. Inicia, lê o news.txt, divide a mensagem em partes (devido ao limite de 2000 caracteres do Discord), publica no canal de destino, e, em seguida, deleta os arquivos news.txt e news.json antes de se desligar.
    
🛠️ Configuração e Instalação
  Pré-requisitos
    Python 3.
    Conta Google AI Studio (para obter a Chave API do Gemini).
    Um bot do Discord criado e tokens associados.
    Dependências (Instalação): pip install discord.py google-genai requests beautifulsoup4
    
Chaves de API e Configurações
  NOTA: Preencha os espaços em branco com suas credenciais e IDs nos respectivos arquivos:
    O que Preencher
    gemini.pyapi_key="" Sua chave da API do Google Gemini.
    bot.py bot.run("") Token do bot Aethos.
    nexus.py bot.run("") Token do bot Nexus.
    bot.pybot.get_channel() O ID numérico do canal de boas-vindas.
    nexus.pybot.get_channel() O ID numérico do canal onde a análise será postada.
    
🏁 Como Iniciar
  Simplesmente execute o script principal do bot do Discord: python bot.py
    O bot Aethos será inicializado, disparando imediatamente o primeiro ciclo de scraping e análise, e, em seguida, entrará no loop de agendamento de 24 horas.
