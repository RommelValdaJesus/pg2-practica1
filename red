  

```markdown
# Calculadora Factorial en Python

## Descripción
Este proyecto implementa una **calculadora factorial** en Python utilizando **Programación Orientada a Objetos (POO)**. La clase `CalculadoraFactorial` extiende la clase base `Calculadora`, que ofrece operaciones matemáticas básicas.

## Instalación
Para utilizar esta calculadora, asegúrate de tener Python instalado en tu sistema.

## Uso
### Implementación con `main`
1. **Importa la clase** `CalculadoraFactorial`:
   ```python
   from calculadora_poo import CalculadoraFactorial
   ```
2. **Define el número y ejecuta la calculadora factorial** en un `main`:
   ```python
   if __name__ == "__main__":
       numero = 6
       calculadora_factorial = CalculadoraFactorial(numero)
       print(calculadora_factorial.calculadora())
   ```
3. **Ejecuta el código** y obtén el resultado del factorial en la terminal.

## Clases y Métodos
### `Calculadora`
Clase base que representa una calculadora simple con operaciones matemáticas como sumar, restar, multiplicar y dividir.

**Métodos importantes**:
- `sumar(a, b)`: Retorna la suma de `a` y `b`.
- `restar(a, b)`: Retorna la resta de `a` y `b`.
- `multiplicar(a, b)`: Retorna la multiplicación de `a` y `b`.
- `dividir(a, b)`: Retorna la división de `a` entre `b`.
- `mostrar_resultado(a, b)`: Muestra el resultado de la operación.

### `CalculadoraFactorial`
Clase que extiende `Calculadora` para calcular el **factorial** de un número.

**Métodos importantes**:
- `calculadora()`: Calcula el factorial del número proporcionado.
- `mostrar_resultado()`: Devuelve el resultado del cálculo factorial.

## Ejemplo de Uso
```python
from calculadora_poo import CalculadoraFactorial

if __name__ == "__main__":
    numero = 6
    calculadora_factorial = CalculadoraFactorial(numero)
    print(calculadora_factorial.calculadora())
```

## Autor
Este código fue desarrollado para ayudar a calcular el factorial de un número utilizando conceptos de **herencia en POO**.

## Licencia
Este proyecto es de código abierto y puedes modificarlo según tus necesidades.
```
¡Ahora tu README incluye la ejecución con `main` para mayor claridad! 🚀 Déjame saber si deseas más mejoras o ajustes. 😃
