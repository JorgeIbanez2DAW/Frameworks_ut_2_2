
""" Programación síncrona vs asíncrona (Pag 56)
Realizar un programa en Python que cree dos funciones que impriman por
pantalla un rango de valores, la primera desde cero hasta el valor
proporcionado y la segunda entre dos valores dados. Además, entre cada
impresión tendrá que esperar un segundo la primera y medio la segunda.
Ejecutar las dos funciones una a continuación de otra.
Realizarlo con un modelo síncrono y con un modelo asíncrono.
Comprobar la siguiente salida. """

import asyncio


async def producer_async(n: int = 20) -> None:
    for i in range(n):
        print(f"Producido: {i}")
        await asyncio.sleep(1)
        # Si necesitara que imprimiese primero worker,
        # deberia poner el await del tiempo antes de imprimir


async def worker_async(i: int = 20, n: int = 40) -> None:
    for i in range(i, n):
        print(f"Worker: {i}")
        await asyncio.sleep(0.5)


async def main() -> None:
    await asyncio.gather(producer_async(5), worker_async())


if __name__ == "__main__":
    asyncio.run(main())
