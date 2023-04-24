import threading

saldo = 100  # saldo inicial de la cuenta bancaria

def operacion_dinero(cantidad, tipo_operacion):
    global saldo
    if tipo_operacion == "ingreso":
        saldo += cantidad
    elif tipo_operacion == "retiro":
        saldo -= cantidad

# Generar procesos de manera concurrente
for i in range(40):
    thread = threading.Thread(target=operacion_dinero, args=(100, "ingreso"))
    thread.start()

for i in range(20):
    thread = threading.Thread(target=operacion_dinero, args=(50, "ingreso"))
    thread.start()

for i in range(60):
    thread = threading.Thread(target=operacion_dinero, args=(20, "ingreso"))
    thread.start()

for i in range(40):
    thread = threading.Thread(target=operacion_dinero, args=(100, "retiro"))
    thread.start()

for i in range(20):
    thread = threading.Thread(target=operacion_dinero, args=(50, "retiro"))
    thread.start()

for i in range(60):
    thread = threading.Thread(target=operacion_dinero, args=(20, "retiro"))
    thread.start()

# Esperar a que todos los hilos finalicen
for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()

# Imprimir saldo final
print("Saldo final:", saldo)
