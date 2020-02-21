#Ejercicio 1.

def ListarCoches(doc):
    modelos=doc.xpath("//modelo//text()")
    marcas=doc.xpath("//marca//text()")
    coches=[]
    for elem,elem1 in zip(modelos,marcas):
        coches.append(elem+elem1)
    cochesnorepetidos=[]
    for i in coches:
        if i not in cochesnorepetidos:
            cochesnorepetidos.append(i)
    return cochesnorepetidos

#Ejercicio 2.

def ContarConcesionarios(doc):
    return len(doc.xpath("/concesionarios[count(coches)>3]"))

#Ejercicio 3.

def CochesPorConcesionario(doc,concesionario):
    modelos=doc.xpath("/concesionarios/concesionario[nombre/text()='%s']/coches/coche/modelo/text()"%concesionario)
    marcas=doc.xpath("/concesionarios/concesionario[nombre/text()='%s']/coches/coche/marca/text()"%concesionario)
    coches=[]
    for elem,elem1 in zip(modelos,marcas):
        coches.append(elem+elem1)