from operaciones import suma, resta, multiplicacion, division

def main():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        op = input("Ingrese la operación (+, -, *, /): ")

        if op == "+":
            resultado = suma(a, b)
        elif op == "-":
            resultado = resta(a, b)
        elif op == "*":
            resultado = multiplicacion(a, b)
        elif op == "/":
            resultado = division(a, b)
        else:
            print("Operador inválido.")
            return

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Error: Entrada no numérica.")
    except ZeroDivisionError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()