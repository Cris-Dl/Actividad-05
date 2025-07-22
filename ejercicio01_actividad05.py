#MENÚ DE ANÁLISIS DE VENTAS
while True:
    print("MENÚ DE ANÁLISIS DE VENTAS")
    print("1. Ingresar lista de ventas (valores enteros positivos)")
    print("2. Mostrar todas las ventas ingresadas")
    print("3. Calcular la venta más alta y la más baja")
    print("4. Calcular promedio de ventas")
    print("5. Contar cuántos días superaron los Q1000")
    print("6. Buscar si una venta específica existe en la lista")
    print("7. Clasificar cada venta: alta (>1000), media (500–1000), baja (<500)")
    print("8. Salir")
    opcion = input("Ingrese el número de la opción que quiera acceder:")
    match opcion:
        case "1":
            print("Ingresar lista de ventas")
        case "2":
            print("Ventas ingresadas")
        case "3":
            print("Calcular la venta más alta y la más baja")
        case "4":
            print("Calcular promedio de ventas")
        case "5":
            print("Contar cuántoss días superaron los Q1000")
        case "6":
            print("Buscar si existe una venta especifica")
        case "7":
            print("Clasificación de ventas")
        case "8":
            print("Esta saliendo del programa")
            break
        case _:
            print("Opción invalida, vuelva a intentar")