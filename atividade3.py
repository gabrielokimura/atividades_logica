class Contabancaria():
    def __init__(self, saldo, titular):
        self.titular=titular
        self.__saldo=saldo

    def depositar(self,valor):
        self.valor=valor
        self.__saldo+=self.valor


    def sacar(self, valor):
        self.valor=valor
        if self.valor<=self.__saldo:
            self.__saldo=self.__saldo-self.valor
        else:
            print("Não há dinheiro suficiente na conta")


            
