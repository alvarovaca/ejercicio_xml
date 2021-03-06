from lxml import etree
from Funciones import *

doc = etree.parse('concesionarios.xml')

print()
print("                                                                         MENÚ                                                                 ")
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print("1. Listar el modelo y marca de todos los coches que se encuentran a la venta junto a sus características.")
print("2. Contar el número de concesionarios que vendan más de 3 coches y en caso de así quererlo, mostrar también sus nombres.")
print("3. Pedir por teclado nombres de concesionarios y listar el nombre de los coches que venden, hasta que se introduzca un espacio.")
print("4. Pedir por teclado un modelo y una marca y mostrar en qué concesionario se puede comprar, además de la ciudad de dicho concesionario.")
print("5. Seleccionar dos coches distintos mediante un menú, para posteriormente mostrar las ventajas de uno sobre el otro.")
print("6. Salir del menú.")
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print()

while True:
    opcion=int(input("Introduce una opción: "))
    while opcion<1 or opcion>6:
        opcion=int(input("La opción introducida no es válida. Vuelve a intentarlo: "))
    if opcion==1:
        print()
        print("-----------------")
        print("LISTADO DE COCHES")
        print("-----------------")
        coches,potencias,puertas,precios,co2s,consumos,velocidades=ListarCoches(doc)
        for elem, elem1, elem2, elem3, elem4, elem5, elem6 in zip(coches,potencias,puertas,precios,co2s,consumos,velocidades):
            print()
            print(elem)
            print()
            print("Su potencia es de", elem1, "CV.")
            print("Tiene", elem2, "puertas.")
            print("Su precio es de", elem3, "€.")
            print("Su emisión de CO2 es de", elem4, "gr/km.")
            print("Su consumo es de", elem5, "litros/100km.")
            print("Su velocidad máxima es de", elem6, "km/h.")
        print()
    elif opcion==2:
        print()
        print("--------------------------")
        print("CONTADOR DE CONCESIONARIOS")
        print("--------------------------")
        print()
        concesionarios=ContarConcesionarios(doc)
        print(len(concesionarios))
        print()
        siono=input("¿Deseas ver el nombre de dichos concesionarios? (S/N): ")
        while ValidarSioNo(siono)!=True:
            siono=input("La respuesta introducida no es válida. Vuelve a intentarlo: ")
        if siono=="S":
            print()
            for i in concesionarios:
                print(i[0])
        print()
    elif opcion==3:
        print()
        print("------------------------")
        print("COCHES POR CONCESIONARIO")
        print("------------------------")
        print()
        while True:
            concesionario=input("Introduce un concesionario: ")
            while ValidarConcesionario(doc, concesionario)!=True and concesionario!=" ":
                concesionario=input("El concesionario introducido no existe. Vuelve a intentarlo: ")
            if concesionario==" ":
                break
            print()
            for i in CochesPorConcesionario(doc, concesionario):
                print(i)
            print()
        print()
    elif opcion==4:
        print()
        print("------------------")
        print("BUSCADOR DE COCHES")
        print("------------------")
        print()
        modelo=input("Introduce un modelo de coche: ")
        marca=input("Introduce una marca de coche: ")
        print()
        concesionarios,ciudades=EnQueConcesionario(modelo,marca,doc)
        if len(concesionarios)>0 and len(ciudades)>0:
            print("El coche introducido se ha encontrado en los siguientes concesionarios:")
            print()
            for elem, elem1 in zip(concesionarios,ciudades):
                print(elem[0], "------", elem1[0])
        else:
            print("No se ha podido encontrar el coche introducido.")
        print()
    elif opcion==5:
        print()
        print("------------------")
        print("SELECCIONAR COCHES")
        print("------------------")
        for contador in range(1,3):
            print()
            for i in ListarConcesionarios(doc):
                print(i)
            print()
            concesionario=input("Introduce un concesionario de los mostrados: ")
            while ValidarConcesionario(doc,concesionario)!=True:
                concesionario=input("El concesionario introducido no existe. Vuelve a intentarlo: ")
            print()
            for i in ListarMarcas(concesionario,doc):
                print(i)
            print()
            marca=input("Introduce una marca de las mostradas: ")
            while ValidarMarca(marca,ListarMarcas(concesionario,doc))!=True:
                marca=input("La marca introducida no existe. Vuelve a intentarlo: ")
            modelos,potencias,puertas,precios,co2s,consumos,velocidades = ListarCochesPorMarca(marca,concesionario,doc)
            for elem,elem1,elem2,elem3,elem4,elem5,elem6 in zip(modelos,potencias,puertas,precios,co2s,consumos,velocidades):
                print()
                print(elem)
                print()
                print("Su potencia es de", elem1, "CV.")
                print("Tiene", elem2, "puertas.")
                print("Su precio es de", elem3, "€.")
                print("Su emisión de CO2 es de", elem4, "gr/km.")
                print("Su consumo es de", elem5, "litros/100km.")
                print("Su velocidad máxima es de", elem6, "km/h.")
            print()
            modelo=input("Introduce un modelo de los mostrados: ")
            while ValidarModelo(modelo,ListarModelos(marca,concesionario,doc))!=True:
                modelo=input("El modelo introducido no existe. Vuelve a intentarlo: ")
            if contador == 1:
                primero=GuardarDatos(marca,modelo,concesionario,doc)
            if contador == 2:
                segundo=GuardarDatos(marca,modelo,concesionario,doc)
        print()
        print("------------------")
        print("RESULTADOS FINALES")
        print("------------------")
        print()
        for i in CompararCoches(primero,segundo):
            print(i)
        print()
    elif opcion==6:
        print()
        print("Gracias por utilizar nuestro menú.")
        print()
        break