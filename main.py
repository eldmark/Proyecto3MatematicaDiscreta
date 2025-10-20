from itertools import permutations, combinations
from collections import Counter
import math

# Funciones para cálculos combinatorios
def factorial(n):
    """Calcula el factorial de n"""
    return math.factorial(n)

def permutaciones_objetos_diferentes(elementos):
    """
    Calcula permutaciones de objetos diferentes.
    P(n) = n!
    """
    n = len(elementos)  # Número de elementos
    formula = f"P({n}) = {n}!"  # Fórmula de permutaciones
    total = factorial(n)  # Cálculo del total de permutaciones
    perms = list(permutations(elementos))  # Generar todas las permutaciones
    
    return {
        'formula': formula,
        'calculo': f"{n}! = {total}",
        'total': total,
        'elementos': perms
    }

def permutaciones_objetos_iguales(elementos):
    """
    Calcula permutaciones de objetos con repetición.
    P(n; n1, n2, ..., nk) = n! / (n1! * n2! * ... * nk!)
    """
    n = len(elementos)  # Número total de elementos
    contador = Counter(elementos)  # Contar ocurrencias de cada elemento
    
    # Construir fórmula
    repeticiones = [f"{elem}:{count}" for elem, count in contador.items() if count > 1]
    denominador_formula = " × ".join([f"{count}!" for count in contador.values()])
    denominador_valores = " × ".join([str(factorial(count)) for count in contador.values()])
    
    formula = f"P({n}; {', '.join(repeticiones)}) = {n}! / ({denominador_formula})"
    
    # Calcular
    numerador = factorial(n)  # Factorial del numerador
    denominador = 1
    for count in contador.values():
        denominador *= factorial(count)  # Producto de factoriales del denominador
    
    total = numerador // denominador  # Total de permutaciones
    
    # Generar permutaciones únicas
    perms = list(set(permutations(elementos)))
    
    calculo = f"{numerador} / {denominador} = {total}"
    
    return {
        'formula': formula,
        'calculo': calculo,
        'total': total,
        'elementos': perms
    }

def combinaciones_objetos_diferentes(elementos, r):
    """
    Calcula combinaciones de objetos diferentes.
    C(n, r) = n! / (r! * (n-r)!)
    """
    n = len(elementos)  # Número total de elementos
    
    if r > n:
        return {
            'error': f"No se pueden seleccionar {r} objetos de un conjunto de {n} elementos"
        }
    
    formula = f"C({n}, {r}) = {n}! / ({r}! × ({n}-{r})!)"
    
    numerador = factorial(n)  # Factorial del numerador
    denominador = factorial(r) * factorial(n - r)  # Factorial del denominador
    total = numerador // denominador  # Total de combinaciones
    
    combs = list(combinations(elementos, r))  # Generar combinaciones
    
    calculo = f"{numerador} / ({factorial(r)} × {factorial(n-r)}) = {total}"
    
    return {
        'formula': formula,
        'calculo': calculo,
        'total': total,
        'elementos': combs
    }

def combinaciones_objetos_iguales(elementos, r):
    """
    Calcula combinaciones de objetos con repetición permitida.
    Usa combinaciones con reemplazo: C(n+r-1, r)
    """
    # Obtener elementos únicos
    elementos_unicos = list(set(elementos))
    n = len(elementos_unicos)  # Número de elementos únicos
    
    if r > len(elementos):
        return {
            'error': f"No se pueden seleccionar {r} objetos de un conjunto de {len(elementos)} elementos"
        }
    
    # Generar todas las combinaciones posibles considerando repeticiones
    combs = list(combinations(elementos, r))
    # Eliminar duplicados convirtiendo a conjuntos ordenados
    combs_unicas = list(set(tuple(sorted(c)) for c in combs))
    
    total = len(combs_unicas)  # Total de combinaciones únicas
    
    # Fórmula para combinaciones con repetición
    formula = f"Combinaciones con repetición de {r} elementos"
    calculo = f"Total de combinaciones únicas: {total}"
    
    return {
        'formula': formula,
        'calculo': calculo,
        'total': total,
        'elementos': combs_unicas
    }

def mostrar_resultados(resultado, mostrar_elementos=True):
    """Muestra los resultados de forma formateada"""
    print(f"\n{'='*60}")
    print(f"Fórmula: {resultado['formula']}")
    print(f"Cálculo: {resultado['calculo']}")
    print(f"Total: {resultado['total']}")
    
    if mostrar_elementos and 'elementos' in resultado:
        print(f"\nElementos ({len(resultado['elementos'])}):")
        for i, elem in enumerate(resultado['elementos'], 1):
            if isinstance(elem, tuple):
                print(f"  {i}. {' '.join(map(str, elem))}")  # Imprimir combinaciones
            else:
                print(f"  {i}. {elem}")  # Imprimir permutaciones
    print(f"{'='*60}\n")

def menu_principal():
    """Menú principal del programa"""
    print("\n" + "="*60)
    print("CALCULADORA DE PERMUTACIONES Y COMBINACIONES")
    print("="*60)
    
    # Entrada de elementos
    entrada = input("\nIngrese los elementos separados por espacios (ej: a b c d): ").strip()
    elementos = entrada.split()  # Separar elementos por espacios
    
    if not elementos:
        print("Error: Debe ingresar al menos un elemento.")
        return
    
    print(f"\nConjunto ingresado: {{{', '.join(elementos)}}}")
    print(f"Total de elementos: {len(elementos)}")
    
    # Verificar si hay elementos repetidos
    tiene_repetidos = len(elementos) != len(set(elementos))
    if tiene_repetidos:
        contador = Counter(elementos)
        print(f"Elementos con repeticiones: {dict(contador)}")
    
    flag = True
    while flag:
        print("\n" + "-"*60)
        print("MENÚ DE OPCIONES:")
        print("1. Permutaciones de objetos diferentes")
        print("2. Permutaciones de objetos iguales")
        print("3. Combinaciones de objetos diferentes")
        print("4. Combinaciones de objetos iguales")
        print("5. Ingresar nuevo conjunto")
        print("6. Salir")
        print("-"*60)
        
        opcion = input("\nSeleccione una opción (1-6): ").strip()
        
        match opcion:
            case '1':
                print("\n*** PERMUTACIONES DE OBJETOS DIFERENTES ***")
                resultado = permutaciones_objetos_diferentes(elementos)
                mostrar = len(resultado['elementos']) <= 50
                if not mostrar:
                    print(f"\n(Hay {resultado['total']} permutaciones. Mostrando solo fórmula y total)")
                mostrar_resultados(resultado, mostrar)

            case '2':
                print("\n*** PERMUTACIONES DE OBJETOS IGUALES ***")
                if not tiene_repetidos:
                    print("\nNota: No hay elementos repetidos. El resultado será igual a permutaciones de objetos diferentes.")
                resultado = permutaciones_objetos_iguales(elementos)
                mostrar = len(resultado['elementos']) <= 50
                if not mostrar:
                    print(f"\n(Hay {resultado['total']} permutaciones. Mostrando solo fórmula y total)")
                mostrar_resultados(resultado, mostrar)

            case '3':
                print("\n*** COMBINACIONES DE OBJETOS DIFERENTES ***")
                try:
                    r = int(input(f"¿Cuántos objetos desea seleccionar? (1-{len(elementos)}): "))
                    resultado = combinaciones_objetos_diferentes(elementos, r)
                    if 'error' in resultado:
                        print(f"\nError: {resultado['error']}")
                    else:
                        mostrar_resultados(resultado, True)
                except ValueError:
                    print("\nError: Debe ingresar un número válido.")

            case '4':
                print("\n*** COMBINACIONES DE OBJETOS IGUALES ***")
                try:
                    r = int(input(f"¿Cuántos objetos desea seleccionar? (1-{len(elementos)}): "))
                    resultado = combinaciones_objetos_iguales(elementos, r)
                    if 'error' in resultado:
                        print(f"\nError: {resultado['error']}")
                    else:
                        mostrar_resultados(resultado, True)
                except ValueError:
                    print("\nError: Debe ingresar un número válido.")

            case '5':
                menu_principal()  # Volver a mostrar el menú principal
                break

            case '6':
                print("\nGracias por usar la calculadora. ¡Hasta luego!")
                flag = False
                break

            case _:
                print("\nOpción inválida. Por favor, seleccione una opción del 1 al 6.")

if __name__ == "__main__":
    menu_principal()  # Ejecutar el menú principal al iniciar el programa
