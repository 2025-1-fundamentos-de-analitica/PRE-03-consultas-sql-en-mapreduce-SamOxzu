"""Taller evaluable"""

# pylint: disable=broad-exception-raised
# pylint: disable=import-error


#
# ORQUESTADOR:
#

# Importamos el sistema mapreduce del archivo mapreduce.py
# import mapreduce.run_mapreduce_job as run_mapreduce_job  # type: ignore
from .mapreduce import run_mapreduce_job
#
# Columns:
# total_bill, tip, sex, smoker, day, time, size
#

#
# SELECT *, tip/total_bill as tip_rate
# FROM tips;
#
def mapper_query_1(sequence):
    """Mapper"""
    result = []
    # Recorre la secuencia de entrada, donde index es el índice y row es la fila.
    # Usamos _ para indicar que no nos interesa el primer valor (el nombre del archivo).
    for index, (_, row) in enumerate(sequence):
        # Si es la primera fila (encabezado), añadimos el encabezado con la nueva columna.
        if index == 0:
            result.append((index, row.strip() + ",tip_rate"))
        else:
            # Descomponemos la fila en componentes (separados por comas).
            row_values = row.strip().split(",")
            # Definimos el componente total_bill como el primer valor
            total_bill = float(row_values[0])
            # Definimos el componente tip como el segundo valor
            tip = float(row_values[1])
            # Calculamos tip_rate como tip/total_bill
            tip_rate = tip / total_bill
            # Añadimos la fila original con la nueva columna tip_rate.
            result.append((index, row.strip() + "," + str(tip_rate)))
    # Una vez procesadas todas las filas, devolvemos la secuencia resultante.
    return result


def reducer_query_1(sequence):
    """Reducer"""
    # En este caso, no se requiere reducción, simplemente devolvemos la secuencia tal cual.
    return sequence

#
# SELECT *
# FROM tips
# WHERE time = 'Dinner';
#
def mapper_query_2(sequence):
    """Mapper"""
    result = []
    # Recorre la secuencia de entrada, donde index es el índice y row es la fila.
    # Usamos _ para indicar que no nos interesa el primer valor (el nombre del archivo).
    for index, (_, row) in enumerate(sequence):
        # Si es la primera fila (encabezado), añadimos el encabezado.
        # En este caso, no se requiere modificación del encabezado.
        if index == 0:
            result.append((index, row.strip()))
        else:
            # Descomponemos la fila en componentes (separados por comas).
            row_values = row.strip().split(",")
            # Comprobamos si el valor de la columna "time" es "Dinner".
            # La columna "time" es la sexta columna (índice 5).
            if row_values[5] == "Dinner":
                # Si es "Dinner", añadimos la fila original a la secuencia resultante.
                # si no, la ignoramos.
                result.append((index, row.strip()))
    # Después de filtrar las filas, devolvemos la secuencia resultante.
    return result


def reducer_query_2(sequence):
    """Reducer"""
    # En este caso, no se requiere reducción, simplemente devolvemos la secuencia tal cual.
    return sequence

#
# SELECT *
# FROM tips
# WHERE time = 'Dinner' AND tip > 5.00;
#
def mapper_query_3(sequence):
    """Mapper"""
    result = []
    # Recorre la secuencia de entrada, donde index es el índice y row es la fila.
    # Usamos _ para indicar que no nos interesa el primer valor (el nombre del archivo).
    for index, (_, row) in enumerate(sequence):
        # Si es la primera fila (encabezado), añadimos el encabezado.
        # En este caso, no se requiere modificación del encabezado.
        if index == 0:
            result.append((index, row.strip()))
        else:
            # Descomponemos la fila en componentes (separados por comas).
            row_values = row.strip().split(",")
            # Hacemos un doble condicional para filtrar las filas donde el
            # valor de la columna "time" es "Dinner" y el valor de la columna "tip" es mayor que 5.00.
            # La columna "time" es la sexta columna (índice 5) y la columna "tip" es la segunda columna (índice 1).
            if row_values[5] == "Dinner" and float(row_values[1]) > 5.00:
                # Si se cumplen ambas condiciones, añadimos la fila original a la secuencia resultante.
                # si no, la ignoramos.
                result.append((index, row.strip()))
    # Después de filtrar las filas, devolvemos la secuencia resultante.
    return result


def reducer_query_3(sequence):
    """Reducer"""
    # En este caso, no se requiere reducción, simplemente devolvemos la secuencia tal cual.
    return sequence

#
# SELECT *
# FROM tips
# WHERE size >= 5 OR total_bill > 45;
#
def mapper_query_4(sequence):
    """Mapper"""
    result = []
    # Recorre la secuencia de entrada, donde index es el índice y row es la fila.
    # Usamos _ para indicar que no nos interesa el primer valor (el nombre del archivo).
    for index, (_, row) in enumerate(sequence):
        # Si es la primera fila (encabezado), añadimos el encabezado.
        # En este caso, no se requiere modificación del encabezado.
        if index == 0:
            result.append((index, row.strip()))
        else:
            # Descomponemos la fila en componentes (separados por comas).
            row_values = row.strip().split(",")
            # Hacemos un doble condicional con OR para filtrar las filas que cumplen alguna
            # de las dos condiciones:
            # 1. La columna "size" es mayor o igual a 5 (índice 6).
            # 2. La columna "total_bill" es mayor que 45 (índice 0).
            if int(row_values[6]) >= 5 or float(row_values[0]) > 45:
                # Si se cumple alguna de las condiciones, añadimos la fila original a la secuencia resultante.
                # si no, la ignoramos.
                result.append((index, row.strip()))
    # Después de filtrar las filas, devolvemos la secuencia resultante.
    # En este caso, no se requiere reducción, simplemente devolvemos la secuencia tal cual.
    return result


def reducer_query_4(sequence):
    """Reducer"""
    # En este caso, no se requiere reducción, simplemente devolvemos la secuencia tal cual.
    return sequence

#
# SELECT sex, count(*)
# FROM tips
# GROUP BY sex;
#
def mapper_query_5(sequence):
    """Mapper"""
    result = []
    # Recorre la secuencia de entrada, donde index es el índice y row es la fila.
    # Usamos _ para indicar que no nos interesa el primer valor (el nombre del archivo).
    for index, (_, row) in enumerate(sequence):
        # Si es la primera fila (encabezado), la ignoramos.
        if index == 0:
            continue
        # Descomponemos la fila en componentes (separados por comas).
        row_values = row.strip().split(",")
        # Añadimos a resultado una tupla con el valor de sex (índice 2)
        # y el valor 1 (para contar).
        result.append((row_values[2], 1))
    # Después de procesar todas las filas, devolvemos la secuencia resultante.
    return result


def reducer_query_5(sequence):
    """Reducer"""
    counter = dict()
    # Recorre la secuencia de entrada, donde key es el valor de sex y value
    # el 1 que nos ayudará a contar.
    for key, value in sequence:
        # Si el key no está en el diccionario (es la primer ocurrencia de ese
        # valor de sex), lo inicializamos a 0.
        if key not in counter:
            counter[key] = 0
        # Sumamos el valor 1 presente en el value a la cuenta de ocurrencias
        counter[key] += value
    # Después de contar todas las ocurrencias, devolvemos a manera de lista el
    # resultado presente en el diccionario counter.
    # La función items() devuelve una vista de los pares clave-valor del diccionario.
    return list(counter.items())

#
# ORQUESTADOR:
#
def run():
    """Orquestador"""

    run_mapreduce_job(
        mapper=mapper_query_1,
        reducer=reducer_query_1,
        input_directory="files/input",
        output_directory="files/query_1",
    )

    run_mapreduce_job(
        mapper=mapper_query_2,
        reducer=reducer_query_2,
        input_directory="files/input",
        output_directory="files/query_2",
    )

    run_mapreduce_job(
        mapper=mapper_query_3,
        reducer=reducer_query_3,
        input_directory="files/input",
        output_directory="files/query_3",
    )

    run_mapreduce_job(
        mapper=mapper_query_4,
        reducer=reducer_query_4,
        input_directory="files/input",
        output_directory="files/query_4",
    )

    run_mapreduce_job(
        mapper=mapper_query_5,
        reducer=reducer_query_5,
        input_directory="files/input",
        output_directory="files/query_5",
    )


if __name__ == "__main__":

    run()