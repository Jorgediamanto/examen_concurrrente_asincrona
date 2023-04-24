import multiprocessing

# Lock object to control access to the shared saldo variable
saldo_lock = multiprocessing.Lock()
saldo = multiprocessing.Value('i', 100)  # saldo inicial de la cuenta bancaria

def operacion_dinero(cantidad, tipo_operacion):
    global saldo
    with saldo_lock:
        if tipo_operacion == "ingreso":
            saldo.value += cantidad
        elif tipo_operacion == "retiro":
            saldo.value -= cantidad

if __name__ == '__main__':
    # Generar procesos de manera concurrente
    for i in range(40):
        p = multiprocessing.Process(target=operacion_dinero, args=(100, "ingreso"))
        p.start()

    for i in range(20):
        p = multiprocessing.Process(target=operacion_dinero, args=(50, "ingreso"))
        p.start()

    for i in range(60):
        p = multiprocessing.Process(target=operacion_dinero, args=(20, "ingreso"))
        p.start()

    for i in range(40):
        p = multiprocessing.Process(target=operacion_dinero, args=(100, "retiro"))
        p.start()

    for i in range(20):
        p = multiprocessing.Process(target=operacion_dinero, args=(50, "retiro"))
        p.start()

    for i in range(60):
        p = multiprocessing.Process(target=operacion_dinero, args=(20, "retiro"))
        p.start()

    # Esperar a que todos los procesos finalicen
    for p in multiprocessing.active_children():
        p.join()

    # Imprimir saldo final
    print("Saldo final:", saldo.value)

