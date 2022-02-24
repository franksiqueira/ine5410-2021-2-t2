from threading import Thread
from time import sleep
from random import randint

import init

class Cliente(Thread):
    '''
        Os clientes (frequentadores do parque) realizam as seguintes ações:
        - Vestir os equipamentos de proteção (macacão, luvas, capacete)
        - Ir a uma das atrações:
            - Pista de patinação no gelo:
                - Pegar patins
                - Aguardar vaga na pista
                - Patinar
            - Teleférico:
                - Pagar uma cadeira livre
                - Subir a montanha
                - Ir para uma das pistas ou permanecer no teleférico
            - Pista de snowboad:
                - Pegar uma prancha
                - Aguardar vaga
                - Descer a montanha
                - Devolver equipamento, caso deixe a atração
            - Pista de esqui:
                - Pegar esquis
                - Aguardar vaga
                - Descer a montanha
                - Devolver equipamento, caso deixe a atração
            - Pistas de trenó (skeleton):
                - Pegar trenó
                - Aguardar pista livre
                - Descer a montanha
                - Devolver o equipamento
            - Pistas de bobsled:
                - Formar dupla
                - Pegar bobsled
                - Aguardar pista livre 
                - Descer a montanha
                - Devolver o equipamento
        - Decidir aleatoriamente se permanece, se vai para outra atração ou vai embora

        Cada uma dessas ações corresponde a um método do cliente. A sua responsabilidade 
        é desenvolver os comportamentos dentro dos métodos do cliente de modo que ele se
        comporte conforme a especificação contida no Moodle.

        Esses métodos são chamados no método run() da classe Cliente.
      
    '''
    # Construtor do nadador
    # Argumentos indicam o gênero e se é criança e aprendiz
    def __init__(self, id):
        self.id     = id

        super().__init__(name=("Cliente " + str(id)))

    # Função que imprime mensagens de log
    def log(self, mensagem):
        espacos = (16 - len(self.name)) * ' '
        print('['+ self.name + '] ' + espacos + mensagem + '\n', end='')

    # Representação do nadador nas mensagens de log
    def __repr__(self):
        return self.name

    # Comportamento do nadador
    def run(self):
        '''
            NÃO ALTERE A ORDEM DAS CHAMADAS ABAIXO.

            Você deve implementar os comportamentos dentro dos métodos invocados. 
            Observação: Comente no código qual o objetivo de uma dada operação, 
            ou conjunto de operações, para facilitar a correção do trabalho.
        '''

        self.log("Entrou no Winter Park.")

        self.pegar_equip_protecao()
        if randint(1,3) == 1:
            # Vai para pista de patinação
            self.pegar_patins()
            self.aguardar_lugar_pista()
            self.patinar()
            if randint(1,3) == 1:

        self.pegar_()
        self.tomar_ducha()
        self.sair_vestiario()
        if self.aprendiz:
            self.pegar_prancha()
        self.pegar_raia()
        self.nadar()
        self.liberar_raia()
        if self.aprendiz:
            self.devolver_prancha()        
        self.entrar_vestiario()
        self.tomar_ducha()
        self.liberar_armario()
        self.trocar_roupa()
        self.sair_vestiario()

        self.log("Saiu do Winter Park.")

    # Nadador entra no vestiário correspondente ao seu gênero
    def entrar_vestiario(self):
        '''
            IMPLEMENTE AQUI:
            O nadador deve entrar no vestiário correspondente ao seu gênero.
        '''
        if self.genero == 'F':
            with init.lock_vest_fem:
                init.cont_vest_fem += 1
        self.log("Entrou no vestiário")

    # Nadador sai do vestiário         
    def sair_vestiario(self):
        '''
            IMPLEMENTE AQUI:
            O nadador deve sair do vestiário.
        '''
        if self.genero == 'F':
            with init.lock_vest_fem:
                init.cont_vest_fem -= 1
                if init.cont_vest_fem == 0:
                    init.vest_fem_vazio.notify()
        self.log("Saiu do vestiário")

    # Nadador troca de roupa 
    def trocar_roupa(self):
        self.log("Trocando de roupa...")
        sleep(randint(init.tempo_troca_min, init.tempo_troca_max) * init.unidade_de_tempo)

    # Nadador encontra um armário e guarda seus pertences
    def pegar_armario(self):
        '''
            IMPLEMENTE AQUI:
            O nadador deve encontrar um armário para guardar os seus pertences.
            O armário precisa estar no vestiário correspondente ao seu gênero.
        '''        
        if self.genero == 'F':
            init.armarios_vest_fem.acquire()
        else:
            init.armarios_vest_masc.acquire()
        self.log("Pegou um armário")

    # Nadador libera o armário
    def liberar_armario(self):
        '''
            IMPLEMENTE AQUI:
            O nadador deve liberar o armário no qual guardou os seus pertences.
        '''        
        if self.genero == 'F':
            init.armarios_vest_fem.release()
        else:
            init.armarios_vest_masc.release()
        self.log("Liberou um armário")

    # Nadador toma uma ducha antes ou depois de nadar
    def tomar_ducha(self):
        '''
            IMPLEMENTE AQUI:
            Encontrar um box livre para tomar ducha.
        '''
        if self.genero == 'F':
            init.duchas_vest_fem.acquire()
        else:
            init.duchas_vest_masc.acquire()        
        self.log("Tomando uma ducha...")
        sleep(randint(init.tempo_ducha_min, init.tempo_ducha_max) * init.unidade_de_tempo)
        self.log("Terminou de tomar uma ducha.")
        '''
            IMPLEMENTE AQUI:
            Liberar a ducha.
        '''
        if self.genero == 'F':
            init.duchas_vest_fem.release()
        else:
            init.duchas_vest_masc.release()         

    # Nadador aprendiz deve pegar uma prancha antes de entrar na piscina
    def pegar_prancha(self):
        '''
            IMPLEMENTE AQUI:
            O nadador aprendiz deve pegar uma prancha para nadar.
        '''
        init.pranchas.acquire()
        self.log("Pegou uma prancha para nadar.")

    # Nadador aprendiz devolve a prancha que estava usando para nadar
    def devolver_prancha(self):
        self.log("Devolvendo uma prancha.")
        '''
            IMPLEMENTE AQUI:
            O nadador aprendiz deve devolver a prancha.
        '''
        init.pranchas.release()
        
    # Nadador tenta encontrar uma raia para nadar    
    def pegar_raia(self):
        '''
            IMPLEMENTE AQUI:
            O nadador deve encontrar uma raia para nadar. Adultos precisam
            de uma raia exclusiva, e 2 crianças podem compartilhar uma raia.
        '''
        with init.lock_piscina:
            if self.crianca == False:
                while init.raias_ocupadas > (init.quant_raias-1) :
                    self.log("Piscina lotada. Aguardando raia ser liberada...")
                    init.raia_livre.wait()
                init.raias_ocupadas += 1
            else:
                while init.raias_ocupadas == init.quant_raias :
                    self.log("Piscina lotada. Aguardando raia ser liberada...")
                    init.raia_livre.wait()
                init.raias_ocupadas += .5
            init.piscina.append(self)
            self.log("Conseguiu uma raia para nadar.")
            self.log("Na piscina: " + str(init.piscina))

    # Nadador libera a raia na qual estava nadando
    def liberar_raia(self):
        self.log("Liberando uma raia.")
        '''
            IMPLEMENTE AQUI:
            O nadador deve liberar a raia.
        '''
        with init.lock_piscina:
            init.piscina.remove(self)
            if self.crianca == False:
                init.raias_ocupadas -= 1
            else:
                init.raias_ocupadas -= .5
            init.raia_livre.notify()

    # Simula o tempo que o nadador fica na piscina nadando
    def nadar(self):
        self.log("Começou a nadar.")
        sleep(randint(init.tempo_nadando_min, init.tempo_nadando_max) * init.unidade_de_tempo)
        self.log("Terminou de nadar.")