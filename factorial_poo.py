from calculadora_poo import Calculadora

class CalculadoraFactorial(Calculadora):
    def __init__(self, numero):
       
        self.numero = numero
        super().__init__()

    def calculadora(self):
        self.__resultado = 1
        cont = 1
        while cont <= int(self.numero):
            self.__resultado = self._multiplicar(self.__resultado, cont)
            cont += 1
        return self.mostrar_resultado()


    def mostrar_resultado(self):
        return f"El factorial de {self.numero} es {self.__resultado}"