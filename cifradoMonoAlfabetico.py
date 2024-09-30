def StringAArray(string):
    array = []
    array[:0] = string
    return(array)

######################################################################################################

def ArrayAString(array):
    string=''.join(array)
    return(string)

######################################################################################################

def upper(letra):
    if letra=="a":
        letra="A"
    elif letra=="b":
        letra="B"
    elif letra=="c":
        letra="C"
    elif letra=="d":
        letra="D"
    elif letra=="e":
        letra="E"
    elif letra=="f":
        letra="F"
    elif letra=="g":
        letra="G"
    elif letra=="h":
        letra="H"
    elif letra=="i":
        letra="I"
    elif letra=="j":
        letra="J"
    elif letra=="k":
        letra="K"
    elif letra=="l":
        letra="L"
    elif letra=="m":
        letra="M"
    elif letra=="ñ":
        letra="Ñ"
    elif letra=="n":
        letra="N"
    elif letra=="o":
        letra="O"
    elif letra=="p":
        letra="P"
    elif letra=="q":
        letra="Q"
    elif letra=="r":
        letra="R"
    elif letra=="s":
        letra="S"
    elif letra=="t":
        letra="T"
    elif letra=="u":
        letra="U"
    elif letra=="v":
        letra="V"
    elif letra=="w":
        letra="W"
    elif letra=="x":
        letra="X"
    elif letra=="y":
        letra="Y"
    elif letra=="z":
        letra="Z"
    return(letra)

######################################################################################################
print("Introduzca texto a descifrar")
texto=input()
print("Texto recibido con exito")
texto = StringAArray(texto)
print("Cambiando todas las minusculas del texto por mayusculas...")
cont=0
for cont in range(0,len(texto)):
    texto[cont]=upper(texto[cont])

print("Todo el texto se encuentra en mayusculas!")

######################################################################################################

print("Calculando numero de apariciones...")
cont=0
alfabeto=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numeroApariciones=c=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for cont in range(0,len(texto)):
    if texto[cont]== "A":
        numeroApariciones[0]=numeroApariciones[0]+1
    elif texto[cont]=="B":
        numeroApariciones[1]=numeroApariciones[1]+1
    elif texto[cont]=="C":
        numeroApariciones[2]=numeroApariciones[2]+1
    elif texto[cont]=="D":
        numeroApariciones[3]=numeroApariciones[3]+1
    elif texto[cont]=="E":
        numeroApariciones[4]=numeroApariciones[4]+1
    elif texto[cont]=="F":
        numeroApariciones[5]=numeroApariciones[5]+1
    elif texto[cont]=="G":
        numeroApariciones[6]=numeroApariciones[6]+1
    elif texto[cont]=="H":
        numeroApariciones[7]=numeroApariciones[7]+1
    elif texto[cont]=="I":
        numeroApariciones[8]=numeroApariciones[8]+1
    elif texto[cont]=="J":
        numeroApariciones[9]=numeroApariciones[9]+1
    elif texto[cont]=="K":
        numeroApariciones[10]=numeroApariciones[10]+1
    elif texto[cont]=="L":
        numeroApariciones[11]=numeroApariciones[11]+1
    elif texto[cont]=="M":
        numeroApariciones[12]=numeroApariciones[12]+1
    elif texto[cont]=="Ñ":
        numeroApariciones[14]=numeroApariciones[14]+1
    elif texto[cont]=="N":
        numeroApariciones[13]=numeroApariciones[13]+1
    elif texto[cont]=="O":
        numeroApariciones[15]=numeroApariciones[15]+1
    elif texto[cont]=="P":
        numeroApariciones[16]=numeroApariciones[16]+1
    elif texto[cont]=="Q":
        numeroApariciones[17]=numeroApariciones[17]+1
    elif texto[cont]=="R":
        numeroApariciones[18]=numeroApariciones[18]+1
    elif texto[cont]=="S":
        numeroApariciones[19]=numeroApariciones[19]+1
    elif texto[cont]=="T":
        numeroApariciones[20]=numeroApariciones[20]+1
    elif texto[cont]=="U":
        numeroApariciones[21]=numeroApariciones[21]+1
    elif texto[cont]=="V":
        numeroApariciones[22]=numeroApariciones[22]+1
    elif texto[cont]=="W":
        numeroApariciones[23]=numeroApariciones[23]+1
    elif texto[cont]=="X":
        numeroApariciones[24]=numeroApariciones[24]+1
    elif texto[cont]=="Y":
        numeroApariciones[25]=numeroApariciones[25]+1
    elif texto[cont]=="Z":
        numeroApariciones[26]=numeroApariciones[26]+1

print("Numero de apariciones calculado!")
    
######################################################################################################

print("Ordenando valores obtenidos de mayor a menor...")

alfa=alfabeto
aparicionesYLetras = list(zip(numeroApariciones, alfabeto))
aparicionesYLetrasOrdenado = sorted(aparicionesYLetras, key=lambda x: x[0], reverse=True)
numeroApariciones, alfabeto = zip(*aparicionesYLetrasOrdenado)

print("Valores obtenidos ordenados!")

######################################################################################################

alfabetoCastellano=["  E  ","  A  ","  O  ","  L  ","  S  ","  N  ","  D  ","  R  ","  U  ","  I  ","  T  ","  C  ","  P  ","  M  ","  Y  ","  Q  ","  B  ","  H  ","  G  ","  F  ","  V  ","  J  ","  Ñ  ","  Z  ","  X  ","  K  ","  W  "]
porcentajeCastellano=["16.78%","11.96%","8.69%","8.37%","7.88%","7.01%","6.87%","4.94%","4.80%","4.15%","3.31%","2.92%","2.776%","2.12%","1.54%","1.53%","0.92","0.89%","0.73%","0.52%","0.39%","0.30%","0.29%","0.15%","0.06%","0.00%","0.00%"]

print("Comenzamos el proceso de descifrado del texto")
fin=False
pos=0
textoc=texto.copy()
while not fin:
    print("#######################################################################################")
    print("Valores obtenidos del texto:")
    print(alfabeto)
    print(numeroApariciones)
    print("#######################################################################################")
    print("Porcentajes del castellano:")
    print(alfabetoCastellano)
    print(porcentajeCastellano)
    print("#######################################################################################")
    #COPIA DEL TEXTO ORIGINAL Y LA COPIA QUE MOSTRAMOS QUE YA NO ESTA EN EL FORMATO ARRAY
    textocm=ArrayAString(textoc)
    print("#######################################################################################")
    print(textocm)
    print("Introduzca la letra en minusculas con el que sustituir " + alfa[pos])
    print("O bien elija otra letra que editar con '1' para retroceder y '2' para avanzar")
    print("Tambien puede escribir 'R' mayuscula para reiniciar los valores introducidos en el texto")
    print("O escriba 'F' mayuscula si ha acabado el decifrado")
    orden=input()
    if orden=="1":
        pos=pos-1
        if pos==-1:
            pos=26
    elif orden=="2":
        pos=pos+1
        if pos==27:
            pos=0
    elif orden=="5":
    #    pos=pos+5
    #    if pos==27:
    #        pos=pos-26
        print(ArrayAString(texto))
    elif orden=="R":
        textoc=texto.copy()
    elif orden=="F":
        fin=True
    else:
        cont=0
        for cont in range(0,len(textoc)):
            if textoc[cont]==alfa[pos]:
                textoc[cont]=orden

print("#######################################################################################")

textocm=ArrayAString(textoc)
print(textocm)
print("Texto descifrado, gracias por confiar en Descifradores Txomin! :D")
