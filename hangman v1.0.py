#import ahorcado_turtle_2 as dibujo
import random

#### VARIABLES GENERALES ################################################################################################

palabras = ["edificio", "casa", "ciudad", "oceano", "Nicaragua"]

contador_letras_fallidas = 0

lista_letras_fallidas = []

perder = False

#ESCOGEME UNA PALABRA ALEATORIAMENTE DE LA LISTA DE PALABRAS
palabra = random.choice(palabras).upper()

################################################ FUNCIONES DEFINIDAS ######################################################

"""FUNCION OCULTA LA PALABRA EN UNA CADENA DE GUIONES"""
def convertir(palabra):
    l = list(palabra)
    c = []
    for i in range(len(l)):
        c.append("_")

    return c


"""FUNCION QUE VALIDA SI LA LETRA ESTA EN LA PALABRA Y DEVUELVE SU O SUS POSICIONES EN UNA LISTA DE ELEMENTOS ENTEROS"""
def retorna_indices(letra, palabra):
    
    caracter_indice = [n for n,x in enumerate(palabra) if x==letra] #l.index(caracter)
    return caracter_indice
    


   
"""FUNCION QUE MUESTRA LOS CARACTERES POR PANTALLA QUE SE ENCUENTRAN EN LA PALABRA"""
def mostrar_caracteres_pantalla(lista_indices, c, letra):
  
    for i in lista_indices:
        c[i] = letra
      
    return c

""" FUNCION QUE DIBUJARA EL PERSONAJE DE ACUERDO AL CONTADOR DE LETRAS FALLIDAS QUE USUALMENTE ES DE 6 A 7 LETRAS"""
def validar_letras_fallidas(contador_letras_fallidas, lista_letras_fallidas):
    #global contador_letras_fallidas
    
    print("\nesa letra no esta en la palabra")
    
    #AGREGAME ESA LETRA A LA LISTA DE LETRAS NO PERTENECIENTES A LA PALABRA
    lista_letras_fallidas.append(letra)
    
    print("LETRAS MENCIONADAS: " + str(set(lista_letras_fallidas)))
    
    ##AQUI LLAMAR A LA FUNCION QUE DIBUJARA AL PERSONAJE
    contador_letras_fallidas += 1
    
    if contador_letras_fallidas == 1:
        pass #dibujo.dibuja_poste()
        print("dibuja poste")
    elif contador_letras_fallidas == 2:
        pass #dibujo.dibuja_cabeza()
        print("dibuja cabeza")
    elif contador_letras_fallidas == 3:
        pass #dibujo.dibuja_cuerpo()
        print("dibuja cuerpo")
    elif contador_letras_fallidas == 4:
        pass #dibujo.dibuja_brazo1()
        print("dibuja brazo izquierdo")
    elif contador_letras_fallidas == 4:
        pass #dibujo.dibuja_brazo2()
        print("dibuja brazo derecho")
    elif contador_letras_fallidas == 5:
        pass #dibujo.dibuja_pierna1()
        print("dibuja pierna izquierda")
    elif contador_letras_fallidas == 6:
        pass #dibujo.dibuja_pierna2()
        print("dibuja pierna derecha")
    else:
        print("dibuja cara")

    return contador_letras_fallidas
        

##################################################################  MAIN ##########################################

def main():
    
    global contador_letras_fallidas
    global letra
    
    #CONVERTIR Y MOSTRAR LA PALABRA OCULTA
    c = convertir(palabra)
    palabra_oculta = " ".join(c)
    print("PALABRA DE " + str(len(c)) + " LETRAS")
    print(palabra_oculta)
    mostrar = c

    while True:

        #PEDILE AL USUARIO QUE INGRESE UNA LETRA
        letra = input("\nIngrese una letra: ").upper()
        #EN CASO QUE INGRESEN UNA EXPRESION SIEMPRE TOMARA EL PRIMER CARACTER
        letra = letra[0]
        
        if letra in palabra:

            # RETORNAME LOS INDICES DONDE ESTA LA LETRA EN LA LISTA
            lista_indices = retorna_indices(letra, palabra)
            
            # MOSTRAME EN PANTALLA LAS LETRAS QUE ENCONTRASTES
            mostrar = mostrar_caracteres_pantalla(lista_indices, c, letra)
            
            # VERIFICAME SI NO HAY CARACTERES OCULTOS Y MOSTRAME LA PALABRA COMPLETA, ENTONCES EL USUARIO GANO
            if "_" not in mostrar:
                perder = False
                print(" ".join(mostrar))
                break

        else:
             
            #CONTAME LAS VECES QUE EL USUARIO HA FALLADO UNA LETRA
            contador_letras_fallidas = validar_letras_fallidas(contador_letras_fallidas, lista_letras_fallidas)

            # VERIFICAME SI LAS OPORTUNIDADES SE ACABARON Y SE COMPLETO LA FIGURA, ENTONCES EL USUARIO PERDIO 
            if contador_letras_fallidas > 6:
                perder = True
                break
            
            #EN CASO QUE EL USUARIO TODAVIA TENGA OPORTUNIDADES QUE SIGA INGRESANDO LETRAS
            continue

        
        print(" ".join(mostrar))
             
    if perder == True:
        print("\n:( NO ACERTO LA PALABRA ")
        print(palabra)
    else:
        print("\nENHORABUENA!!! DESCIFRASTES LA PALABRA OCULTA")


### LLAMADA AL PROGRAMA MAIN PRINCIPAL #########################################################################
if __name__=='__main__':
    main()
