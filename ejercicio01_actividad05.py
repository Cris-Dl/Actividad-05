#MENÚ DE ANÁLISIS DE VENTAS
lista_price = []
while True:
    print("MENÚ DE ANÁLISIS DE VENTAS")
    print("1. Ingresar lista de ventas (valores enteros positivos)")
    print("2. Mostrar todas las ventas ingresadas")
    print("3. Calcular la venta más alta y la más baja")
    print("4. Calcular promedio de ventas")
    print("5. Contar cuántos días superaron los Q1000")
    print("6. Clasificar cada venta: alta (>1000), media (500–1000), baja (<500)")
    print("7. Salir")
    opcion = input("Ingrese el número de la opción que quiera acceder:")
    print()
    match opcion:
        case "1":
            print("Ingresar lista de ventas")
            days_prices = int(input("Ingrese la cantidad de días: "))
            if days_prices > 0:
                for i in range(days_prices):
                    user_price = input("Ingrese el precio de cada venta: ")
                    if user_price.isdigit():
                        price_int = int(user_price)
                        lista_price.append(price_int)
                    else:
                        print("Valor invalido vuelva a intentar")
                        while True:
                            user_price = input("Ingrese el precio de cada venta: ")
                            if user_price.isdigit():
                                price_int = int(user_price)
                                lista_price.append(price_int)
                                break
                            else:
                                print("Valor invalido, vuelva a intentar")
        case "2":
            print("Ventas ingresadas")
            print(lista_price)
            print()
        case "3":
            print("Calcular la venta más alta y la más baja")
            print("Venta Máxima:Q", max(lista_price))
            print("Venta Mínima:Q", min(lista_price))
            print()
        case "4":
            print("Calcular promedio de ventas")
            total_price = sum(lista_price)
            total_sales = len(lista_price)
            print("El promedio de ventas fue de:Q", total_price/total_sales)
            print()
        case "5":
            print("Contar cuántos días superaron los Q1000")
            print()
        case "6":
            print("Clasificación de ventas")
            print()
        case "7":
            print("Esta saliendo del programa")
            print()
            break
        case _:
            print("Opción invalida, vuelva a intentar")
            print()
