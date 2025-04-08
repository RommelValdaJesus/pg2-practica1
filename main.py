from calculadora_poo import Calculadora 
from factorial_poo import CalculadoraFactorial

print("Calculadora Estandar")
calculadora_1 = Calculadora()
print(calculadora_1.sumar(5, 6))
print(calculadora_1.restar(15, 8))
print(calculadora_1.multiplicar(65, 6))
print(calculadora_1.dividir(565, 65)) 

print("Calculadora Factorial")
cal_factorial1 = CalculadoraFactorial(5)
print(cal_factorial1.calculadora())