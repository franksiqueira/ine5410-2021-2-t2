import init

class Atracao:
    '''
        Atração representa uma atração do parque. 
        Você deve implementar os métodos que controlam a entrada e saída de
        clientes, respeitando as restrições impostas no enunciado do trabalho.
 
        Observação: Comente no código qual o objetivo de uma dada operação, 
        ou conjunto de operações, para facilitar a correção do trabalho.   
    '''        
    # Construtor da classe que representa uma atração do parque
    def __init__(self, nome_atracao, capacidade_atracao):
        self.nome = nome_atracao              # Nome da atração
        self.capacidade = capacidade_atracao  # Limite de clientes na atração
        
    def entrar_atracao(self):
        '''
            IMPLEMENTE AQUI: Entrada do cliente na atração
        '''

    def sair_atracao(self):
        '''
            IMPLEMENTE AQUI: Saída do cliente da atracao
        '''     