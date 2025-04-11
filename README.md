Aquí tienes tu README corregido con mejoras en la redacción y ortografía:

---

# Práctica 1: Implementación de una Calculadora en Python  

En esta práctica, se implementa una calculadora en Python con capacidad para realizar operaciones matemáticas básicas como suma, resta, multiplicación y división. Además, se extiende su funcionalidad para calcular el factorial de un número, aplicando conceptos de herencia y polimorfismo.  

## Preparación del entorno y ejecución  

Clonar el repositorio:  

```sh
git clone https://github.com/RommelValdaJesus/pg2-practica1.git
cd pg2-practica1
```

Crear un entorno virtual:  

```sh
python -m venv env
```

Activar el entorno virtual:  

En Windows:  

```sh
.\env\Scripts\activate
```  

En Linux o Mac:  

```sh
source env/bin/activate
```

Ejecutar el script:  

```sh
python main.py
```

Desactivar el entorno virtual:  

```sh
deactivate
```

## Implementación de la Calculadora Estándar  

Este módulo implementa una calculadora estándar que permite realizar operaciones aritméticas básicas.  

### Modo de uso  

```python
from calculadora_poo import Calculadora  

calculadora_1 = Calculadora()  
print(calculadora_1.sumar(5, 6))  
print(calculadora_1.restar(15, 8))  
print(calculadora_1.multiplicar(65, 6))  
print(calculadora_1.dividir(565, 65))  
```
## Clases y Métodos
## Calculadora
Clase base que representa una calculadora simple con operaciones matemáticas como sumar, restar, multiplicar y dividir.
Métodos importantes:

- sumar(a, b): Retorna la suma de a y b.
- restar(a, b): Retorna la resta de a y b.
- multiplicar(a, b): Retorna la multiplicación de a y b.
- dividir(a, b): Retorna la división de a entre b.
- mostrar_resultado(a, b): Muestra el resultado de la operación.

CalculadoraFactorial
Clase que extiende Calculadora para calcular el factorial de un número.

## Métodos importantes:
- calculadora(): Calcula el factorial del número proporcionado.
- mostrar_resultado(): Devuelve el resultado del cálculo factorial.


### Modo de uso  

```python
from factorial_poo import CalculadoraFactorial  

cal_factorial1 = CalculadoraFactorial(5)  
print(cal_factorial1.calcular())  
```
## Licencia
Este proyecto utiliza una Licencia MIT.

---
