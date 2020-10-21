"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from App import controller
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


Archivo = 'us_accidents_small.csv'

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Requerimento 1")
    print("4- Requerimento 2")
    print("0- Salir")
    print("*******************************************")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        accidentes= controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de crimenes ....")
        controller.loadData(accidentes,Archivo)
        print('Accidentes cargados: ' + str(controller.sizeAccidentes(accidentes)))
        print('Fechas cargadas: ' + str(controller.sizeArbol(accidentes)),"\n")

    elif int(inputs[0]) == 3:
        Fecha=input('Ingrese la fecha de busqueda (YYYY-MM-DD)\n>: ')
        print("\nBuscando accidentes en la fecha... ")
        tamaño,lista=controller.Dar_cantidad_por_fecha(accidentes,Fecha)
        print("\nSe encontraron",tamaño,"accidentes registrados en la fecha",Fecha)
        iterador=it.newIterator(lista)
        while it.hasNext(iterador):
            element=it.next(iterador)
            Severidad=element["Severidad"]
            size=lt.size(element["Lista_Accidentes"])
            print("Hay", size, " acccidentes reportados con severidad: ",Severidad)
        

    elif int(inputs[0]) == 4:
        print("\nAccidentes antes de una fecha: ")
        Fecha=input("Ingrese la fecha desde la que quiere conocer los accidentes (YYYY-MM-DD): ")
        print("Buscando accidentes...")
        tamaño,lista=controller.Dar_cantidad_fecha_adelante(accidentes,Fecha)
        print("\nSe encontraron",tamaño,"accidentes registrados desde ",Fecha)

    else:
        sys.exit(0)
sys.exit(0)
