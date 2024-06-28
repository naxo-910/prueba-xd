contador=0
contador2=0
n=1

def Comprar_pasajes(pasajeros):
    print("""------menu de compra-------
          (1) comprar  boleto de vuelo
          (2) compre mas de 1 boleto de vuelo
          (3) ingrese rut de la persona
         
          """)
    try:
        respues_compra=int(input("selecione una opcion disponible "))
        if respues_compra==1:
            un_pasaje=int(input("ingrese el numero 1 para confirmar su compra "))
            contador=contador+1
            print("""---tipo de compra---
                (1) Asiento_común
                (2) Añadir Espacio adicional para piernas
                (3) No reclina""")
            rect=int(input("ingrese su opcion disponible"))
            if rect==1:
                print("añadio un asiento comun")
                contador2=Asiento_común+1
            elif rect==2:
                print("añadio un Espacio adicional para piernas")
                contador2=Espacio_adicional_para_piernas+1
            elif rect==3:
                print("añadio No reclina")
                contador2=No_reclina+1
                
        elif respues_compra==2:
            while True:
                mas_pasajes=int(input("ingrese el numero 1 para confirmar su compra "))
                print("se a registrado correctmente")
                n=n+1
                respues_22=int(input("desea comprar otro pasaje?\n(1)si \n(2)no"))
                if respues_22=="2":
                    break 
                print("""---tipo de compra---
                (1) Asiento_común
                (2) Añadir Espacio adicional para piernas
                (3) No reclina""")
            rect=int(input("ingrese su opcion disponible"))
            if rect==1:
                print("añadio un asiento comun")
                contador2=Asiento_común+1
            elif rect==2:
                print("añadio un Espacio adicional para piernas")
                contador2=Espacio_adicional_para_piernas+1
            elif rect==3:
                print("añadio No reclina")
                contador2=No_reclina+1

        elif respues_compra==3:
            rut=int(input("ingrese el rut del pasajero sin puntos ni guin "))
            print("se a registrado correctmente")
    except:
        print("INVALIDO, vuelva a ingreasar e digito")

        Asiento_común=60000
        Espacio_adicional_para_piernas=80000
        No_reclina=50000

        pasajeros.append({
            'compra por un pasaje': un_pasaje,
            'compra po mas de 1 pasaje': mas_pasajes,
            'rut de cliente': rut,
            'valor de asiento comun': Asiento_común,
            'valor de espcio adicional para piernas': Espacio_adicional_para_piernas,
            'valo de no reclina': No_reclina
            })

def Mostrar_ubicaciones_disponibles(pasajeros):
    pass

def Ver_listado_de_pasajeros(pasajeros):
    print("listar pasajeros")
    for pasa in pasajeros:
        print(pasa)

def Buscar_pasajero(pasajeros):
    rtu=int(input("ingrese el rut del pasajeo que desea busca(rut in puntos no guion)"))
    for rtu in pasajeros['rut de cliente']:
        print(f"su pasajero es {pasajeros['rut de cliente']}")

def Reasignar_asiento(pasajeros):
    pass

def Mostrar_ganancias_totales(pasajeros):
    pass
