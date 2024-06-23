
# Inicializar el contador

contador = 0

while contador < 3:
    temperatura = float(input('Ingrese la temperatura: '))

    humedad = float(input('Ingrese la humedad: '))

    if temperatura > 30:
        if humedad >= 30:
            accion = "Se recomienda ventilación"
        else:
            accion = "Se recomienda riego y ventilación"
    else:
        if humedad < 30:
            accion = "Solo se recomienda riego"
        else:
            accion = "No se necesitan acciones"

    print(accion)

    contador += 1