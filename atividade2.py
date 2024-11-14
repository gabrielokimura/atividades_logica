class Carro():
    def __init__(self,marca, modelo, ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano

    def exibir_detalhes(self):
        print("marca:",self.marca,"\nModelo:",self.modelo,"\nAno:", self.ano)


carro1=Carro("Toyota","V360",1990)
carro2=Carro("Ferrari","NJ1930", 2020)

carro1.exibir_detalhes()
carro2.exibir_detalhes()