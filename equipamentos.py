import init

class Equipamentos:
    '''
        Equipamentos representa um conjunto de equipamentos de um determinado tipo. 
        Você deve implementar os métodos que controlam a entrega e devolução de
        equipamentos, respeitando as restrições impostas no enunciado do trabalho.
    '''    
    # Construtor da classe que representa um conjunto de equipamentos
    def __init__(self, nome_equipamento, quant_equipamentos):
        self.nome = nome_equipamento
        self.quantidade = quant_equipamentos
        
    def pegar_equipamento(self):
        '''
            IMPLEMENTE AQUI: Entrega de um equipamento
        '''

    def devolver_equipamento(self):
        '''
            IMPLEMENTE AQUI: Devolução de um equipamento
        '''                
