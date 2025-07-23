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
            while True:
                days_prices = input("Ingrese la cantidad de días: ")
                if days_prices.isdigit():
                    day_int = int(days_prices)
                    for i in range(day_int):
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
                    break
                else:
                    print("Valor invalido de días")
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
            max_days = 0
            for i in lista_price:
                if i > 1000:
                    max_days += 1
            if max_days == 0:
                print("No hubo ni un día que superará los Q1000")
            else:
                print("La cantidad de días que superaron los Q1000 fueron de", max_days)
            print()
        case "6":
            print("Clasificación de ventas")
            max_sale, media_sale, min_sale = [], [], []
            for i in lista_price:
                if i >0 and i < 500:
                    min_sale.append(i)
                elif i >= 500 and i <= 1000:
                    media_sale.append(i)
                else:
                    max_sale.append(i)
            print("Ventas altas:", max_sale)
            print("ventas medias: ", media_sale)
            print("Ventas bajas: ", min_sale)
            print()
        case "7":
            print("Esta saliendo del programa, gracias por su preferencia")
            print()
            break
        case _:
            print("Opción invalida, vuelva a intentar")
            print()
