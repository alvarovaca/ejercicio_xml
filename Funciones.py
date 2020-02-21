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
        coches.append(elem+elem1)
    return coches, potencias, puertas, precios, co2s, consumos, velocidades

#Ejercicio 2.

def ContarConcesionarios(doc):
    concesionarios=doc.xpath("/concesionarios")
    concesionariosmastres=[]
    for i in concesionarios:
        if len(i.xpath("./coches"))>3:
            concesionariosmastres.append(i.xpath("./nombre/text()"))
    return concesionariosmastres

#Ejercicio 3.

def CochesPorConcesionario(doc,concesionario):
    modelos=doc.xpath("/concesionarios/concesionario[nombre/text()='%s']/coches/coche/modelo/text()"%concesionario)
    marcas=doc.xpath("/concesionarios/concesionario[nombre/text()='%s']/coches/coche/marca/text()"%concesionario)
    coches=[]
    for elem,elem1 in zip(modelos,marcas):
        coches.append(elem+elem1)
    return coches

#Funciones extra.

def ValidarConcesionario(doc,concesionario):
    if concesionario in doc.xpath("/concesionarios/concesionario/nombre/text()"):
        return True