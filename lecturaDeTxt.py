#-------abro el archivo-------
file=open('datos.txt')
#-------creo la Lista (Importante: 1 string con 3 datos por elemento de la lista)-------
listaFile=file.readlines()
listaLectura=[]
tamañoLista=len(listaFile)
#print(tamañoLista)

#-------Averiguo las Posiciones de las tabulaciones en una sola cadena-------
cadena=listaFile[0]
posiciones=[]
for i in range(len(cadena)):
    if cadena[i]=='\t':
        posiciones.append(i)

print("Las POSISIONES de las tabulaciones en las cadenas son: ")
print(posiciones)    

#-------Recorro la lista y de cada cadena recorto los datos para guardarlo en ListaLectura-------
for i in range(tamañoLista):
    cadena=listaFile[i]

    listaLectura.append((cadena[0:posiciones[0]]).strip())

    listaLectura.append((cadena[posiciones[0]+1:posiciones[1]]).strip())
    
    listaLectura.append((cadena[posiciones[1]+1:posiciones[2]]).strip())

print("-------INFORMACION-------")


#-------Mostrar la lista de elementos-------
#print(listaLectura)

#-------Muestro la cantidad de elementos
print("La CANTIDAD de elementos es: ")
print(len(listaLectura))

#-------Muestro el PRIMER y ULTIMO elemento de la lista
print("El PRIMER elemento es: ")
print(listaLectura[0])
print("El ULTIMO elemento es: ")
print(listaLectura[11114])