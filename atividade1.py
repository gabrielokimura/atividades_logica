class Pessoa ():
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade
    def exibir_detalhes(self):
        print("Meu nome é",self.nome,"e tenho", self.idade,"anos")
    

pessoa1=Pessoa("jorge",22)
pessoa2=Pessoa("Mariana", 55)

pessoa1.exibir_detalhes()
pessoa2.exibir_detalhes()
    
