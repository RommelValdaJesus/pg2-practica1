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
## Uso
### Implementación con `main`
1. **Importa la clase** `CalculadoraFactorial`:
   ```python
   from calculadora_poo import CalculadoraFactorial
   ```
2. **Define el número y ejecuta la calculadora factorial** en un `main`:
   ```python
   if __name__ == "__main__":
       calculadora_factorial = CalculadoraFactorial(5)
       print(calculadora_factorial.calculadora())
   ```
3. **Ejecuta el código** y obtén el resultado del factorial en la terminal.

## Clases y Métodos
## `Calculadora`
Clase base que representa una calculadora simple con operaciones matemáticas como sumar, restar, multiplicar y dividir.

Métodos importantes:

- sumar(a, b): Retorna la suma de a y b.
- restar(a, b): Retorna la resta de a y b.
- multiplicar(a, b): Retorna la multiplicación de a y b.
- dividir(a, b): Retorna la división de a entre b.
- mostrar_resultado(a, b): Muestra el resultado de la operación.

### Modo de uso  

```python
from calculadora_poo import Calculadora  

calculadora_1 = Calculadora()  
print(calculadora_1.sumar(5, 6))  
print(calculadora_1.restar(15, 8))  
print(calculadora_1.multiplicar(65, 6))  
print(calculadora_1.dividir(565, 65))  
```
### `CalculadoraFactorial`
Clase que extiende `Calculadora` para calcular el **factorial** de un número.

## Métodos importantes:
- calculadora(): Calcula el factorial del número proporcionado.
- mostrar_resultado(): Devuelve el resultado del cálculo factorial.


### Modo de uso  

```python
from factorial_poo import CalculadoraFactorial  

cal_factorial1 = CalculadoraFactorial(5)  
print(cal_factorial1.calcular())  
```
## Autor
Este código fue desarrollado para ayudar a calcular el factorial de un número utilizando conceptos de **herencia en POO**.

## Licencia
Este proyecto utiliza una Licencia MIT.

---
