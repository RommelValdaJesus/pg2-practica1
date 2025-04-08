
# clase base que repressenta una calculadora simple (abstracción)
class Calculadora:
    def __init__(self):
        self.__resultado = 0
        self.operacion = ""

    def _mostrar_operacion(self):
        return f'{self.operacion}:{self. a} y {self.b} = {self.__resultado}'   
    
    def mostrar_operaciones(self):
        return f'{self._sumar()}\n{self._restar()}\n{self._multiplicar()}\n{self._dividir()}\n'

    def sumar(self, a, b):
        self.operacion = "sumar"
        self.__resultado = a + b
        return self.mostrar_resultado(a, b)
    
    def restar(self,a, b):
        self.operacion = "restar"
        self.__resultado = a - b
        return self.mostrar_resultado(a, b)
    
    def _multiplicar(self, a, b):
        return a * b
    
    def multiplicar(self, a, b):
        self.operacion = "multiplicar"
        self.__resultado = self._multiplicar(a, b)
        return self.mostrar_resultado(a, b)
    
    def dividir(self, a, b):
        self.operacion = "dividir"
        self.__resultado = a / b
        return self.mostrar_resultado(a, b)
    
    def mostrar_resultado(self, a, b):
        return f"El resultado de {self.operacion} entre {a}, {b} es {self.__resultado}"