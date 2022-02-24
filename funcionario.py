from threading import Thread
from time import sleep

import init

class Funcionario(Thread):
    '''
        Nadadores devem ser criados periodicamente e realizar as seguintes ações:
        - Limpar os vestiários masculino e feminino.
        - Descansar.

        A sua responsabilidade é implementar os métodos com o comportamento do
        funcionário, respeitando as restrições impostas no enunciado do trabalho.
      
    '''

    # Construtor da classe Funcionario
    def __init__(self, id):
        self.id     = id
        self.genero = 'M'
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
            self.limpar_vest_masculino()
            self.limpar_vest_feminino()
            self.descansar()

        self.log("Terminando o expediente")

    # Funcionário limpa o vestiário masculino. O vestiário não precisa estar vazio.
    def limpar_vest_masculino(self):
        self.log("Iniciando limpeza do vestiário masculino")
        sleep(init.tempo_limpeza_vestiario * init.unidade_de_tempo)
        '''
            IMPLEMENTE AQUI:
            Aguarde que todas as duchas sejam liberadas.
        '''
        for i in range(init.quant_duchas_por_vestiario):
            init.duchas_vest_masc.acquire()
        sleep(init.quant_duchas_por_vestiario * init.tempo_limpeza_ducha * init.unidade_de_tempo)
        self.log("Concluída a limpeza do vestiário masculino")
        '''
            IMPLEMENTE AQUI:
            Libere as duchas para uso.
        '''        
        for i in range(init.quant_duchas_por_vestiario):
            init.duchas_vest_masc.release()

    # Funcionário limpa o vestiário feminino. ATENÇÃO: o vestiário precisa estar vazio!!!
    def limpar_vest_feminino(self):
        '''
            IMPLEMENTE AQUI:
            Aguarde que o vestiário feminino esteja vazio para entrar.
        '''
        init.lock_vest_fem.acquire()
        while init.cont_vest_fem != 0 :
            init.vest_fem_vazio.wait()
            
        self.log("Iniciando limpeza do vestiário feminino")
        sleep(init.tempo_limpeza_vestiario * init.unidade_de_tempo)
        sleep(init.quant_duchas_por_vestiario * init.tempo_limpeza_ducha * init.unidade_de_tempo)
        self.log("Concluída a limpeza do vestiário feminino")
        '''
            IMPLEMENTE AQUI:
            Libere o acesso ao vestiário feminino.
        '''
        init.lock_vest_fem.release()

    # Funcionário descansa durante um tempo
    def descansar(self):
        self.log("Hora do intervalo de descanso.")
        sleep(init.tempo_descanso * init.unidade_de_tempo)
        self.log("Fim do intervalo de descanso.")