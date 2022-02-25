from threading import Thread
from time import sleep

import init

class Funcionario(Thread):
    '''
        Funcionário deve realizar as seguintes ações:
        - Limpar os equipamentos.
        - Descansar.

        A sua responsabilidade é implementar os métodos com o comportamento do
        funcionário, respeitando as restrições impostas no enunciado do trabalho.
      
    '''

    # Construtor da classe Funcionario
    def __init__(self, id):
        self.id     = id
        self.trabalhando = False

        super().__init__(name=("Funcionario " + str(id)))

    # Imprime mensagem de log
    def log(self, mensagem):
        espacos = (16 - len(self.name)) * ' '
        print('['+ self.name + '] ' + espacos + mensagem + '\n', end='')

    # Comportamento do Funcionario
    def run(self):
        '''
            NÃO ALTERE A ORDEM DAS CHAMADAS ABAIXO.

            Você deve implementar os comportamentos dentro dos métodos da classe.
            Observação: Comente no código qual o objetivo de uma dada operação, 
            ou conjunto de operações, para facilitar a correção do trabalho.
        '''
        self.log("Iniciando o expediente")
        self.trabalhando = True     

        while self.trabalhando == True :
            self.limpar_equipamentos()
            self.descansar()

        self.log("Terminando o expediente")

    # Funcionário limpa os equipamentos.
    def limpar_equipamentos(self):
        sleep(init.tempo_limpeza_equipamento * init.unidade_de_tempo)
        '''
            IMPLEMENTE AQUI:
        '''

    # Funcionário descansa durante um tempo
    def descansar(self):
        self.log("Hora do intervalo de descanso.")
        sleep(init.tempo_descanso * init.unidade_de_tempo)
        self.log("Fim do intervalo de descanso.")