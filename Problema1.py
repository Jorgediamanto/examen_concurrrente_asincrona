import threading

saldo = 100  # saldo inicial de la cuenta bancaria

def ingresar_dinero(cantidad):
    global saldo
    saldo += cantidad

def retirar_dinero(cantidad):
    global saldo
    saldo -= cantidad

# Generar procesos que ingresan dinero
for i in range(40):
    thread = threading.Thread(target=ingresar_dinero, args=(100,))
    thread.start()

for i in range(20):
    thread = threading.Thread(target=ingresar_dinero, args=(50,))
    thread.start()

for i in range(60):
    thread = threading.Thread(target=ingresar_dinero, args=(20,))
    thread.start()

# Generar procesos que retiran dinero
for i in range(40):
    thread = threading.Thread(target=retirar_dinero, args=(100,))
    thread.start()

for i in range(20):
    thread = threading.Thread(target=retirar_dinero, args=(50,))
    thread.start()

for i in range(60):
    thread = threading.Thread(target=retirar_dinero, args=(20,))
    thread.start()

# Esperar a que todos los hilos finalicen
for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()

# Imprimir saldo final
print("Saldo final:", saldo)
