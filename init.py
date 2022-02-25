from threading import Semaphore, Lock, Condition
from time import sleep
from random import randint
import sys, argparse

from cliente import *
from funcionario import *

# Limites de tempo para criação de clientes e uso das atrações
tempo_cliente_min           = 5
tempo_cliente_max           = 15
tempo_atracao_min           = 10
tempo_atracao_max           = 20

# Quantidades de recursos do parque
quant_equip_individuais     = 10
quant_patins                = 5
quant_esquis                = 5
quant_snowboards            = 4
quant_bobsleds              = 2
quant_trenos                = 6 

# Parâmetros do funcionário
tempo_limpeza_equipamento   = 5
tempo_descanso              = 10

# Tempo total de simulação. Encerrado esse tempo, não crie mais clientes.
tempo_total                 = 1000

# Uma unidade de tempo de simulação. Quanto menor, mais rápida a execução.
unidade_de_tempo            = 0.1 # 100ms

# Varíaveis e estruturas globais necessárias para implementação do programa
teleferico = []                   # Adicione todos os clientes que estão no teleferico a essa lista
cadeiras_ocupadas = 0             # Registre quantas cadeiras do teleférico estão em uso

# Defina aqui outras varíaveis e estruturas globais necessárias para implementação do programa

if __name__ == "__main__":
    # Verifica a versão do python
    if sys.version_info < (3, 0):
        sys.stdout.write('Utilize python3 para desenvolver este trabalho\n')
        sys.exit(1)

    # Processa os argumentos de linha de comando
    parser = argparse.ArgumentParser()
    parser.add_argument("--unidade_de_tempo", "-u", help="valor da unidade de tempo de simulação")
    parser.add_argument("--tempo_total", "-t", help="tempo total de simulação")
    parser.add_argument("--tempo_cliente_min", "-tcmin", help="tempo mínimo para entrada de clientes")
    parser.add_argument("--tempo_cliente_max", "-tcmax", help="tempo máximo para entrada de clientes")
    parser.add_argument("--tempo_atracao_min", "-tamin", help="tempo mínimo para uso de uma atração")
    parser.add_argument("--tempo_atracao_max", "-tamax", help="tempo máximo para uso de uma atração")

    args = parser.parse_args()
    if args.unidade_de_tempo:
        unidade_de_tempo = float(args.unidade_de_tempo)
    if args.tempo_total:
        tempo_total = int(args.tempo_total)
    if args.tempo_cliente_min:
        tempo_cliente_min = int(args.tempo_cliente_min)
    if args.tempo_cliente_max:
        tempo_cliente_max = int(args.tempo_cliente_max)
    if args.tempo_atracao_min:
        tempo_atracao_min = int(args.tempo_atracao_min)
    if args.tempo_atracao_max:
        tempo_atracao_max = int(args.tempo_atracao_max)

    # Tempo desde a abertura do parque
    tempo = 0

    # IMPLEMENTE AQUI: crie as varíaveis locais usadas pelo programa
    clientes = []                 # Adicione todos os clientes que entraram no parque
    cont_clientes = 0             # Contador de clientes que entraram no parque

    # IMPLEMENTE AQUI: Criação do funcionário
    func = Funcionario('João')
    func.start()
  
    # Enquanto o tempo total de simuação não for atingido
    while tempo < tempo_total:
        # IMPLEMENTE AQUI: Criação de um cliente, usando valores aleatórios
        cont_clientes += 1
        cliente = Cliente(cont_clientes)
        cliente.start()
        clientes.append(cliente)

        # Aguarda um tempo aleatório antes de criar o próximo cliente
        intervalo = randint(tempo_cliente_min, tempo_cliente_max)  
        sleep(intervalo * unidade_de_tempo)     
        # Atualiza a variável tempo considerando o intervalo de criação dos cliente
        tempo += intervalo

    # Faça o funcionário parar de trabalhar assim que terminar o que estiver fazendo  
    func.trabalhando = False

    # Aguarde a finalização (término) de todos os clientes e do funcionário 
    # antes de finalizar a execução do programa.
    for cliente in clientes:
        cliente.join()

    func.join()

