
# clase base que repressenta una calculadora simple (abstracción)
class Calculadora:
    def __init__(self, a, b):
        self.__resultado = 0
        self.operacion = ""
        self.a = a
        self.b = b

    def _mostrar_operacion(self):
        return f'{self.operacion}:{self. a} y {self.b} = {self.__resultado}'   
    
    def mostrar_operaciones(self):
        return f'{self._sumar}\n{self._resta}\n{self._multiplicacion}\n{self._division}\n'
    

    def _sumar(self):
        self.operacion = "sumar"
        self.__resultado = self.a + self.b
        return self._mostrar_operacion()
    
    def _resta(self):
        self.operacion = "resta"
        self.__resultado = self.a - self.b
        return self._mostrar_operacion()
    
    def _multiplicacion(self):
        self.operacion = "multiplicacion"
        self.__resultado = self.a * self.b
        return self._mostrar_operacion()
    
    def _division(self):
        self.operacion = "division"
        self.__resultado = self.a / self.b
        return self._mostrar_operacion()
    
    
    


calculadora_1 = Calculadora(15, 5)


print(calculadora_1.mostrar_operaciones())