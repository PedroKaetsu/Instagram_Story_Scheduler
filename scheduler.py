import os
import time
import datetime
import sched
import storyPoster

# Varre o diretório e insere os arquivos para agendamento
def procurar_arquivos(diretorio):
    arquivos_encontrados = []
    for root, dirs, files in os.walk(diretorio):
        for file in files:
            arquivos_encontrados.append(os.path.join(root, file))
    return arquivos_encontrados

# Agenda os jobs para serem executados conforme data, que é o próprio nome do arquivo
def agendar_tarefas(arquivos):
    s = sched.scheduler(time.time, time.sleep)
    for arquivo in arquivos:
        # Converte o nome do arquivo (epoch) para datetime
        data_epoch = int(os.path.splitext(os.path.basename(arquivo))[0])
        data = datetime.datetime.utcfromtimestamp(data_epoch)
        print(data)
        # Agendando a tarefa para a data especificada
        s.enterabs(data.timestamp(), 1, executar_tarefa, argument=(arquivo,))
    s.run()

# Chama o storyPoster para realização do Post
def executar_tarefa(arquivo):
    # É passado o path absoluto do arquivo para a função
    storyPoster.post(os.path.abspath(arquivo))

# Diretório inicial
diretorio = 'stories/'
# Procurar arquivos no diretório
arquivos_encontrados = procurar_arquivos(diretorio)

if arquivos_encontrados:
    print("Arquivos encontrados:")
    for arquivo in arquivos_encontrados:
        print(arquivo)
    # Agendar tarefas para execução nas datas especificadas pelos arquivos encontrados
    print("Agendando tarefas...")
    agendar_tarefas(arquivos_encontrados)
else:
    print("Nenhum arquivo encontrado para agendamento.")

