class Pessoa:
    #Metodo construtor
    def __init__(self, nome, idade, comendo=False, falando=False):
        #Atributos que pode ser comparado as variaveis
        #Para fins didaticos
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
    #Metodo simples 
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já esta comendo.')
            return
        print(f'{self.nome} esta comendo {alimento}.')
        self.comendo = True
    #Metodo simples
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não esta comendo.')
            return
    #metodo simples 
    def falar(self):
        print('Pessoa esta falando....')
            
        