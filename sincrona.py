
""" Programación síncrona vs asíncrona (Pag 56)
Realizar un programa en Python que cree dos funciones que impriman por
pantalla un rango de valores, la primera desde cero hasta el valor
proporcionado y la segunda entre dos valores dados. Además, entre cada
impresión tendrá que esperar un segundo la primera y medio la segunda.
Ejecutar las dos funciones una a continuación de otra.
Realizarlo con un modelo síncrono y con un modelo asíncrono.
Comprobar la siguiente salida. """

import time


def producer(n: int = 20):
    for i in range(n):
        print(f"Producido: {i}")
        time.sleep(1)


def worker(i: int = 20, n: int = 40):
    for i in range(i, n):
        print(f"Worker: {i}")
        time.sleep(0.5)


def main():
    producer(5)
    worker()


if __name__ == "__main__":
    main()
