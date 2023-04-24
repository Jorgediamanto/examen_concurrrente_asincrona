import threading
import time
import random

saldo_jugadores = [1000] * 12    # 4 jugadores para cada estrategia
saldo_banca = 50000

def verificar_saldo():
    global saldo_jugadores, saldo_banca
    total_jugadores = sum(saldo_jugadores)
    if total_jugadores > saldo_banca:
        return False
    else:
        return True



def jugar_a_numero(numero):
    global saldo_jugadores, saldo_banca
    while True:
        time.sleep(3)
        apuesta = 10
        saldo_jugadores[numero] -= apuesta
        resultado = random.randint(0, 36)
        if resultado == numero:
            saldo_jugadores[numero] += 36 * apuesta
            if verificar_saldo():
                saldo_banca -= 36 * apuesta
            else:
                print("La banca no puede cubrir todas las apuestas realizadas.")
            
        else:
            saldo_banca += apuesta

def jugar_a_paridad(par):
    global saldo_jugadores, saldo_banca
    while True:
        time.sleep(3)
        apuesta = 10
        saldo_jugadores[4 + par] -= apuesta
        resultado = random.randint(0, 36)
        if resultado == 0:
            saldo_jugadores[4 + par] += apuesta
            
        elif resultado % 2 == par:
            saldo_jugadores[4 + par] += 20
            if verificar_saldo():
                saldo_banca -= 20
            else:
                print("La banca no puede cubrir todas las apuestas realizadas.")
            
        else:
            saldo_banca += apuesta

def jugar_a_martingala(numero):
    global saldo_jugadores, saldo_banca
    while True:
        time.sleep(3)
        apuesta = 10
        saldo_jugadores[8 + numero] -= apuesta
        resultado = random.randint(0, 36)
        if resultado == numero:
            saldo_jugadores[8 + numero] += 36 * apuesta
            if verificar_saldo():
                saldo_banca -= 36 * apuesta
            else:
                print("La banca no puede cubrir todas las apuestas realizadas.")
            
        else:
            saldo_banca += apuesta
            apuesta *= 2
            while apuesta < saldo_jugadores[8 + numero]:
                saldo_jugadores[8 + numero] -= apuesta
                resultado = random.randint(0, 36)
                if resultado == numero:
                    saldo_jugadores[8 + numero] += 36 * apuesta
                    if verificar_saldo():
                        saldo_banca -= 36 * apuesta
                    else:
                        print("La banca no puede cubrir todas las apuestas realizadas.")
                    apuesta = 10
                    break
                else:
                    saldo_banca += apuesta
