import math, statistics

def letras_multiplos():
    print("\n"+"AAABBB: ")
    for i in range(1, 10):#Me genera una lista de valores consecutivos
        #print(i)
        if i % 3 == 0:
            print('AAA')
        elif i % 5 == 0:
            print('BBB')
        elif i % 5 == 0 and i % 3 == 0:
            print('AAA BBB')
        else:
            print(i)

def factorial():
    print("\n"+"Factorial: ")
    print(math.factorial(4))

def media():
    print("\n"+"Media: ")
    #lista = [i for i in range(1, 100)]
    lista = [4,36,45,50,75]
    print(lista)
    print(statistics.mean(lista))

def intersection():
    print("\n"+"Intersection: ")
    lista_1 = [1, 2, 4, 6, 10]
    lista_2 = [2, 4, 5, 7, 10]
    lista_vac= []
    for i in lista_1:
        for j in lista_2:
            if i==j:
                lista_vac.append(i)
    print(lista_vac)

def suma_dos():
    print("\n"+"Suma_dos: ")
    print("Primera Lista: ")
    lista_1 = [1, 2, 3, 4]
    for i in lista_1:
        print('i: ',i)
        for j in lista_1:
            print('j: ',j)
            if i == j:
                #print("Son iguales i: ",i," y la j: ",j,"-No se evalua-" )
                continue#Este keyword hace que interrumpa la iteracion y avance a la siguiente
            elif i+j == 5:
                print("Cuando i es: ",i,"y "+"j es: ",j,"El resultado es True")
    
    print("Segunda Lista: ")
    lista_2 = [3, 4, 6]
    for i in lista_2:
        print('i: ',i)
        for j in lista_2:
            print('j: ',j)
            if i == j:
                #print("Son iguales i: ",i," y la j: ",j,"-No se evalua-" )
                continue
            elif i+j == 6:
                print("Cuando i es: ",i,"y "+"j es: ",j,"El resultado es True")
            else:
                print("False")

    print("Termina Suma_dos")

def contar():
    print("\n"+"Contar: ")
    diccionario ={}
    contador = 0
    lista = [1, 3, 2, 1, 5, 3, 5, 1, 4]
    while (len(lista)) > 0:
        print ("Lista a evaluar: ",lista)
        iterador = lista[0]
        print("Valor a contar: ",iterador)
        contador = lista.count(iterador)#count es un metodo que cuenta los valores que se repiten en un lista
        diccionario[iterador] = contador
        print("Diccionario con conteo:",diccionario)
        print("Se elimina de la lista a: ", iterador)
        lista = [i for i in lista if i != iterador]#List Comprehension
    for key,value in diccionario.items():
        print("Se repite el ",key,":",value,"veces/vez")

def borra_duplicados():
    print("\n"+"Borra_duplicados: ")
    #lista_1 = [1, 2, 3, 2]
    #lista_2 = [1, 2, 2, 1, 5, 3, 2, 1, 4]
    super_lista = [[1, 2, 3, 2],[1, 2, 2, 1, 5, 3, 2, 1, 4]]
    lista_vacia = []
    print("\n"+"Super Lista con duplicados:", super_lista)
    for lista in super_lista:
        print("\n"+"Tamaño de lista actual: ",len(lista))
        print("Lista: ",lista)
        iterador = 0
        posicion_mov = iterador + 1
        while len(lista) > posicion_mov:#9 > 0-8
            # print("\n"+"Evaluamos condiciones en : ")
            # print("iterador: ", iterador)
            # print("posicion_mov: ", posicion_mov)
            if lista[iterador] != lista[posicion_mov]:#Iterador y posicion_mov recorren la misma lista, se iguala sus valores en sus respectivas posiciones 
                posicion_mov +=1 #Cuando se llega al ultimo valor de la lista este desborda la posicion por lo tanto el codigo se para
                # print("\n"+"Se salta una posicion, no se elimina elemento de la lista, tamaño de lista: ",len(lista))
                # print("Nueva posicion: ", posicion_mov)
                if posicion_mov == len(lista):#Esto es para resetear contadores
                    print("\n"+"Tamaño y Posicion son iguales (CASO 1), se actualiza 'iterador' y 'posicion_mov'")
                    iterador +=1
                    posicion_mov = iterador + 1
                    # print("Nueva posicion por reseteo: ", posicion_mov )#Cuando esta posicion sea igual al tamaño de la lista se rompe el bucle
                    # print("Tamaño actual de lista en el reseteo : ",len(lista))
            else:
                print("\n"+"Se va a eliminar el elemento de la posicion actual que es: ",posicion_mov," de la lista: ",lista)
                del lista[posicion_mov]
                # print("\n"+"Se elimino elemento de posicion actual y queda la lista como: ",lista)
                # print("Tamaño de lista: ",len(lista))
                # print("No se actualiza 'posicion_mov'")
                if posicion_mov == len(lista):#Esto es para resetear contadores
                    print("\n"+"Tamaño y Posicion son iguales (CASO 2), se actualiza 'iterador' y 'posicion_mov'")
                    iterador +=1
                    posicion_mov = iterador + 1
                    # print("Nueva posicion por reseteo: ", posicion_mov )#Cuando esta posicion sea igual al tamaño de la lista se rompe el bucle
                    # print("Tamaño actual de lista en el reseteo : ",len(lista))
        print("\n"+"Se rompe el bucle porque no se cumple la condicion del bucle 'while' dado que Nueva posicion es: ",posicion_mov )        
        print("Lista sin duplicados: ",lista)
        lista_vacia.append(lista)
    print("\n"+"Super Lista sin duplicados:", lista_vacia)

if __name__ == '__main__':
    letras_multiplos()
    factorial()
    media()
    intersection()
    suma_dos()
    contar()
    borra_duplicados()


    


    