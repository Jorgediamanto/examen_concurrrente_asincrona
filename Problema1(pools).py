import multiprocessing

# Lock object to control access to the shared saldo variable
saldo_lock = multiprocessing.Lock()
saldo = multiprocessing.Value('i', 100)  # saldo inicial de la cuenta bancaria

def operacion_dinero(args):
    global saldo
    cantidad, tipo_operacion = args
    with saldo_lock:
        if tipo_operacion == "ingreso":
            saldo.value += cantidad
        elif tipo_operacion == "retiro":
            saldo.value -= cantidad

if __name__ == '__main__':
    with multiprocessing.Pool(processes=6) as pool:
        ingresos = [(100, "ingreso")] * 40 + [(50, "ingreso")] * 20 + [(20, "ingreso")] * 60
        retiros = [(100, "retiro")] * 40 + [(50, "retiro")] * 20 + [(20, "retiro")] * 60
        pool.map(operacion_dinero, ingresos + retiros)

    # Imprimir saldo final
    print("Saldo final:", saldo.value)
