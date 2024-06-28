import funcion as fn 

pasajeros=[]


while True:
    print("""----aerolineas Flash-------
        (1) Comprar pasajes
        (2) Mostrar ubicaciones disponibles
        (3) Ver listado de pasajeros
        (4) Buscar pasajero
        (5) Reasignar asiento
        (6) Mostrar ganancias totales
        (7) salir""")
    try:
        opc_menu=int(input("sleccione una opcion dispoible"))
        if opc_menu==1:
            fn.Comprar_pasajes(pasajeros)
        elif opc_menu==2:
            fn.Mostrar_ubicaciones_disponibles(pasajeros)
        elif opc_menu==3:
            fn.Ver_listado_de_pasajeros(pasajeros)
        elif opc_menu==4:
            fn.Buscar_pasajero(pasajeros)
        elif opc_menu==5:
            fn.Reasignar_asiento(pasajeros)
        elif opc_menu==6:
            fn.Mostrar_ganancias_totales(pasajeros)
        elif opc_menu==7:
            print("haz salido del programa")
            break
        else:
            print("ingresa una opcion dsiponible ")
    except:
        print("valor invalido ")

