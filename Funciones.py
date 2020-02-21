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