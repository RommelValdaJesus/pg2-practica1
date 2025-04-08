## Práctica 1: 
## Implementación de Calculadora en Python
En esta práctica se implementa una calculadora en Python con capacidad para realizar operaciones matemáticas básicas como suma, resta, multiplicación y división. Además, se extiende su funcionalidad para calcular el factorial de un número aplicando conceptos de herencia y polimorfismo

## Estructura y Funcionamiento


## Implementación de Calculadora Estándar
Este módulo implementa una calculadora estándar que permite realizar operaciones aritméticas básicas.
Modo de uso:

```python
from calculadora_poo import Calculadora 

calculadora_1 = Calculadora()
print(calculadora_1.sumar(5, 6))
print(calculadora_1.restar(15, 8))
print(calculadora_1.multiplicar(65, 6))
print(calculadora_1.dividir(565, 65)) 
```

## Implementación  de la Calculadora Factorial 
Este módulo amplía la funcionalidad de la calculadora permitiendo calcular el factorial de un número entero positivo.
Uso del módulo:

```python
from factorial_poo import CalculadoraFactorial

cal_factorial1 = CalculadoraFactorial(5)
print(cal_factorial1.calculadora())
``` 