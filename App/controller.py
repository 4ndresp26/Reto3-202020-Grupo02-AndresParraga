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

import config as cf
from App import model
import datetime
import csv
from DISClib.DataStructures import listiterator as it
from DISClib.ADT import orderedmap as om


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion del modelo.
    """
    lista_acc=model.New_list()
    return lista_acc


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(accidentes, Archivo):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    Archivo = cf.data_dir + Archivo
    input_file = csv.DictReader(open(Archivo, encoding="utf-8"),
                                delimiter=",")
    for Accidente in input_file:
        model.añadirAccidente(accidentes, Accidente)
    return accidentes
    
# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def sizeArbol(lista_acc):
    size=model.size_Arbol(lista_acc)
    return size

def Dar_cantidad_por_fecha(accidentes,Fecha):
    initialDate = datetime.datetime.strptime(Fecha, '%Y-%m-%d')
    size,lista= model.Accidente_Fecha_severidad(accidentes,initialDate.date())
    return size,lista

def Dar_cantidad_fecha_adelante(accidentes,Fecha):
    initialDate = datetime.datetime.strptime(Fecha, '%Y-%m-%d')
    finalDate=om.minKey(accidentes["Fechas"])
    lista= model.rango_accidentes_severidad(accidentes,finalDate,initialDate.date())
    return lista

def rango_horas(accidentes,inicial,final):
    inicial = datetime.datetime.strptime(inicial, '%H:%M')
    final = datetime.datetime.strptime(final, '%H:%M')
    lista= model.rango_accidentes_hora(accidentes,inicial.date(),final.date())
    return lista
    
def sizeAccidentes(accidentes):
    size=model.tamaño_Accidentes(accidentes)
    return size
