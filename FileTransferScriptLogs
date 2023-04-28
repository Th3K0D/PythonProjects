import os
import shutil
import time
from datetime import datetime
import sys

# Define os diretórios de origem e destino dos arquivos a serem transferidos
pasta_origem = '\\Pasta de origem'
pasta_destino = '\\Pasta destino'
pasta_logs = 'C:\\Logs_Do_Sistema'

# Define o intervalo de tempo entre as transferências de arquivos
intervalo = 180

# Função para reiniciar o programa
def reiniciar_programa():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# Função para registrar logs
def registrar_log(mensagem):
    agora = datetime.now()
    data_formatada = agora.strftime('%Y-%m-%d')
    hora_formatada = agora.strftime('%H:%M:%S')
    nome_arquivo = f"log_{data_formatada}.txt"
    caminho_arquivo = os.path.join(pasta_logs, nome_arquivo)
    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(f"[{hora_formatada}] {mensagem}\n")

# Registra o início do programa nos logs
registrar_log("Programa iniciado")

# Loop principal
while True:
    # Lista todos os arquivos e pastas na pasta de origem
    arquivos = os.listdir(pasta_origem)

    # Inicializa a variável que conta o número de arquivos transferidos
    num_arquivos = 0

    # Loop para cada arquivo na pasta de origem
    for arquivo in arquivos:
        # Monta os caminhos de origem e destino dos arquivos
        caminho_origem = os.path.join(pasta_origem, arquivo)
        caminho_destino = os.path.join(pasta_destino, arquivo)

        # Tenta mover o arquivo ou pasta para o destino
        try:
            # Verifica se o caminho é um diretório ou arquivo e move para o destino
            if os.path.isdir(caminho_origem):
                shutil.move(caminho_origem, caminho_destino)
            else:
                shutil.move(caminho_origem, caminho_destino)
                # Incrementa a variável de contagem de arquivos transferidos
                num_arquivos += 1
        # Se ocorrer um erro ao transferir o arquivo, exibe uma mensagem de erro
        except Exception as e:
            registrar_log(f"Ocorreu um erro ao transferir o arquivo {arquivo}: {e}")

    # Obtém a hora atual e exibe a mensagem de status com a quantidade de arquivos transferidos
    agora = datetime.now()
    mensagem_status = f"Loop executado em {agora.strftime('%d/%m/%Y %H:%M:%S')}. {num_arquivos} arquivos transferidos."
    print(mensagem_status)
    registrar_log(mensagem_status)
    
    # Aguarda o intervalo de tempo definido antes de executar o próximo loop
    time.sleep(intervalo)
