
    
def mostrarmenu():
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")

print("BIENVENIDO")

saldo = 1000 
operaciones = int(input("¿CUÁNTAS OPERACIONES DESEA REALIZAR?: "))

for i in range(operaciones):
    mostrarmenu()
    operacion = input("DIGITE EL NUMERO DE LA OPERACION: ")

    if operacion == "3":
        deposito = float(input("¿Cuánto vas a depositar?: "))
        saldo += deposito
        print(f"Has depositado {deposito}")

    elif operacion == "2":
        retiro = float(input("¿Cuánto vas a retirar?: "))
        if retiro <= saldo:
            saldo -= retiro
            print(f"Has retirado {retiro}")
        else:
            print("No tienes suficiente saldo")

    elif operacion == "1":
        print(f"Tu saldo actual es: {saldo}")

    else:
        print("Opción inválida")
    
    print("Gracias por usar el cajero automático")
