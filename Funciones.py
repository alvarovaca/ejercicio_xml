#Ejercicio 1.

def ListarCoches(doc):
    modelos=doc.xpath("//modelo/text()")
    marcas=doc.xpath("//marca/text()")
    potencias=doc.xpath("//potencia/text()")
    puertas=doc.xpath("//puertas/text()")
    precios=doc.xpath("//precio/text()")
    co2s=doc.xpath("//co2/text()")
    consumos=doc.xpath("//consumo/text()")
    velocidades=doc.xpath("//velmax/text()")
    coches=[]
    for elem,elem1 in zip(modelos,marcas):
        coches.append(elem1+" "+elem)
    return coches, potencias, puertas, precios, co2s, consumos, velocidades

#Ejercicio 2.

def ContarConcesionarios(doc):
    concesionarios=doc.xpath("/concesionarios/concesionario")
    concesionariosmastres=[]
    for i in concesionarios:
        if len(i.xpath("./coches/coche"))>3:
            concesionariosmastres.append(i.xpath("./nombre/text()"))
    return concesionariosmastres

#Ejercicio 3.

def CochesPorConcesionario(doc,concesionario):
    modelos=doc.xpath("/concesionarios/concesionario[nombre/text()='%s']/coches/coche/modelo/text()"%concesionario)
    marcas=doc.xpath("/concesionarios/concesionario[nombre/text()='%s']/coches/coche/marca/text()"%concesionario)
    coches=[]
    for elem,elem1 in zip(modelos,marcas):
        coches.append(elem1+" "+elem)
    return coches

#Ejercicio 4.

def EnQueConcesionario(modelo,marca,doc):
    coche=marca+" "+modelo
    nombres=[]
    ciudades=[]
    concesionarios=doc.xpath("/concesionarios/concesionario")
    for i in concesionarios:
        coches=[]
        modelos=i.xpath("./coches/coche/modelo/text()")
        marcas=i.xpath("./coches/coche/marca/text()")
        for elem,elem1 in zip(modelos,marcas):
            coches.append(elem1+" "+elem)
        if coche in coches:
            nombres.append(i.xpath("./nombre/text()"))
            ciudades.append(i.xpath("./ciudad/text()"))
    return nombres,ciudades

#Ejercicio 5.

def ListarConcesionarios(doc):
    concesionarios=doc.xpath("/concesionarios/concesionario/nombre/text()")
    return concesionarios

def ListarMarcas(concesionario,doc):
    marcas=doc.xpath("/concesionarios/concesionario[nombre/text()='%s']/coches/coche/marca/text()"%concesionario)
    marcassinrepetir=[]
    for i in marcas:
        if i not in marcassinrepetir:
            marcassinrepetir.append(i)
    return marcassinrepetir

def ListarCochesPorMarca(marca,concesionario,doc):
    modelos=doc.xpath("/concesionarios/concesionario[nombre/text()='"+concesionario+"']/coches/coche[marca/text()='"+marca+"']/modelo/text()")
    potencias=doc.xpath("/concesionarios/concesionario[nombre/text()='"+concesionario+"']/coches/coche[marca/text()='"+marca+"']/potencia/text()")
    puertas=doc.xpath("/concesionarios/concesionario[nombre/text()='"+concesionario+"']/coches/coche[marca/text()='"+marca+"']/puertas/text()")
    precios=doc.xpath("/concesionarios/concesionario[nombre/text()='"+concesionario+"']/coches/coche[marca/text()='"+marca+"']/precio/text()")
    co2s=doc.xpath("/concesionarios/concesionario[nombre/text()='"+concesionario+"']/coches/coche[marca/text()='"+marca+"']/co2/text()")
    consumos=doc.xpath("/concesionarios/concesionario[nombre/text()='"+concesionario+"']/coches/coche[marca/text()='"+marca+"']/consumo/text()")
    velocidades=doc.xpath("/concesionarios/concesionario[nombre/text()='"+concesionario+"']/coches/coche[marca/text()='"+marca+"']/velmax/text()")
    return modelos, potencias, puertas, precios, co2s, consumos, velocidades

def ListarModelos(marca,concesionario,doc):
    modelos=doc.xpath("/concesionarios/concesionario[nombre/text()='"+concesionario+"']/coches/coche[marca/text()='"+marca+"']/modelo/text()")
    return modelos

def GuardarDatos(marca,modelo,concesionario,doc):
    potencia=doc.xpath("/concesionarios/concesionario[nombre/text()='"+concesionario+"']/coches/coche[marca/text()='"+marca+"' and modelo/text()='"+modelo+"']/potencia/text()")
    puertas=doc.xpath("/concesionarios/concesionario[nombre/text()='"+concesionario+"']/coches/coche[marca/text()='"+marca+"' and modelo/text()='"+modelo+"']/puertas/text()")
    precio=doc.xpath("/concesionarios/concesionario[nombre/text()='"+concesionario+"']/coches/coche[marca/text()='"+marca+"' and modelo/text()='"+modelo+"']/precio/text()")
    co2=doc.xpath("/concesionarios/concesionario[nombre/text()='"+concesionario+"']/coches/coche[marca/text()='"+marca+"' and modelo/text()='"+modelo+"']/co2/text()")
    consumo=doc.xpath("/concesionarios/concesionario[nombre/text()='"+concesionario+"']/coches/coche[marca/text()='"+marca+"' and modelo/text()='"+modelo+"']/consumo/text()")
    velocidad=doc.xpath("/concesionarios/concesionario[nombre/text()='"+concesionario+"']/coches/coche[marca/text()='"+marca+"' and modelo/text()='"+modelo+"']/velmax/text()")
    return marca, modelo, potencia, puertas, precio, co2, consumo, velocidad, concesionario

def CompararCoches(primero,segundo):
    veredicto=[]
    if int(primero[2][0]) > int(segundo[2][0]):
        veredicto.append("El "+primero[0]+" "+primero[1]+" "+"("+primero[8]+")"+" tiene una potencia superior al "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+").")
    elif int(primero[2][0]) == int(segundo[2][0]):
        veredicto.append("El "+primero[0]+" "+primero[1]+" "+"("+primero[8]+")"+" tiene la misma potencia que el "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+").")
    else:
        veredicto.append("El "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+")"+" tiene una potencia superior al "+primero[0]+" "+primero[1]+" "+"("+primero[8]+").")
    if int(primero[3][0]) > int(segundo[3][0]):
        veredicto.append("El "+primero[0]+" "+primero[1]+" "+"("+primero[8]+")"+" tiene un mayor número de puertas que el "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+").")
    elif int(primero[3][0]) == int(segundo[3][0]):
        veredicto.append("El "+primero[0]+" "+primero[1]+" "+"("+primero[8]+")"+" tiene las mismas puertas que el "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+").")
    else:
        veredicto.append("El "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+")"+" tiene un mayor número de puertas que el "+primero[0]+" "+primero[1]+" "+"("+primero[8]+").")
    if float(primero[4][0]) > float(segundo[4][0]):
        veredicto.append("El "+primero[0]+" "+primero[1]+" "+"("+primero[8]+")"+" es más caro que el "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+").")
    elif float(primero[4][0]) == float(segundo[4][0]):
        veredicto.append("El "+primero[0]+" "+primero[1]+" "+"("+primero[8]+")"+" tiene el mismo precio que el "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+").")
    else:
        veredicto.append("El "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+")"+" es más caro que el "+primero[0]+" "+primero[1]+" "+"("+primero[8]+").")
    if int(primero[5][0]) > int(segundo[5][0]):
        veredicto.append("El "+primero[0]+" "+primero[1]+" "+"("+primero[8]+")"+" contamina más que el "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+").")
    elif int(primero[5][0]) == int(segundo[5][0]):
        veredicto.append("El "+primero[0]+" "+primero[1]+" "+"("+primero[8]+")"+" contamina lo mismo que el "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+").")
    else:
        veredicto.append("El "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+")"+" contamina más que el "+primero[0]+" "+primero[1]+" "+"("+primero[8]+").")
    if float(primero[6][0]) > float(segundo[6][0]):
        veredicto.append("El "+primero[0]+" "+primero[1]+" "+"("+primero[8]+")"+" consume más que el "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+").")
    elif float(primero[6][0]) == float(segundo[6][0]):
        veredicto.append("El "+primero[0]+" "+primero[1]+" "+"("+primero[8]+")"+" consume lo mismo que el "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+").")
    else:
        veredicto.append("El "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+")"+" consume más que el "+primero[0]+" "+primero[1]+" "+"("+primero[8]+").")
    if int(primero[7][0]) > int(segundo[7][0]):
        veredicto.append("El "+primero[0]+" "+primero[1]+" "+"("+primero[8]+")"+" es más rápido que el "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+").")
    elif int(primero[7][0]) == int(segundo[7][0]):
        veredicto.append("El "+primero[0]+" "+primero[1]+" "+"("+primero[8]+")"+" es igual de rápido que el "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+").")
    else:
        veredicto.append("El "+segundo[0]+" "+segundo[1]+" "+"("+segundo[8]+")"+" es más rápido que el "+primero[0]+" "+primero[1]+" "+"("+primero[8]+").")
    return veredicto

#Funciones extra.

def ValidarConcesionario(doc,concesionario):
    if concesionario in doc.xpath("/concesionarios/concesionario/nombre/text()"):
        return True

def ValidarSioNo(siono):
    if siono=="S" or siono=="N":
        return True

def ValidarMarca(marca,marcas):
    if marca in marcas:
        return True

def ValidarModelo(modelo,modelos):
    if modelo in modelos:
        return True