"""
En en una escuela de 1000 alumnos, se han evaluado literatura, matemática y biología, obteniéndose los siguientes resultados:
680 aprobaron literatura. Los datos de la evaluación de Literatura se registraron en un
diccionario:
Literatura = {"Romántica": 40, "Clásica": 118, "Fantástica": 50, "Moderna": 95,
 "Antigüa": 56, "Poesía": 131, "Cuento": 87, "Novela": 103}
320 aprobaron biología. Los datos de la evaluación de Biología se registraron en una tupla:
Biologia = (40, 50, 60, 75, 34, 61)
490 aprobaron matemática. Los datos de la evaluación de Matemática se registraron en una
lista:
Matematica = [34, 40, 61, 75, 87, 90, 103]
Responder: 
a. cuántos aprobaron biología matemática y literatura.         # 1. declaraciones
b. cuántos aprobaron sólo literatura y matemática?             # 2. definir funciones de control (opcional) y otras (necesarias)
c. cuántos aprobaron sólo literatura?                          # 3. convertir en set las estructuras
d. cuántos aprobaron solo biología?                            # 4. Resolver las preguntas y resto de opciones para armar el gráfico 
e. cuántos aprobaron sólo matemática?                          # 5. Definir diagrama de Venn, gráfico y respuestas.
f. cuántos aprobaron 2 de los 3 exámenes?
A modo de sugerencia se indican los pasos ordenados para la solución: 
"""


from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

diccionario_Literatura = {"Romántica": 40, "Clásica": 118, "Fantástica": 50, "Moderna": 95,
  "Antigüa": 56, "Poesía": 131, "Cuento": 87, "Novela": 103}
tupla_Biologia = (40, 50, 60, 75, 34, 61)
lista_matematica = [34, 40, 61, 75, 87, 90, 103]



Matematica = set(lista_matematica)
Biologia = set(tupla_Biologia)

def set_Literatura(diccionario_Literatura):
    literatura = set()
    for elemento in diccionario_Literatura.values():
        literatura.add(elemento)
    return literatura

literatura= set_Literatura(diccionario_Literatura)


def Biologia_Matematica_Literatura(b,m, l):

    return (b &  m & l)



Biologia_Matematica_Literatura = Biologia_Matematica_Literatura(Biologia, Matematica, literatura)




def inters_matenatica_literatura (m, l):

    return (m & l)


inters_matenatica_literatura = inters_matenatica_literatura (Matematica, literatura)



def sololiteratura(b, m, l):

    return (l - b) & (l -  m)



sololiteratura = sololiteratura(Biologia, literatura, Matematica)


def solomatematica(b, m, l):

    return (m  - b) & (m - l)

solomatematica = solomatematica(Biologia, literatura, Matematica)


def solobiologia(b, m, l):

    return (b - l) & (b - m)


solobiologia = solobiologia(Biologia, literatura, Matematica)

def biologia_literatura(b, l):

    return (b & l)

biologia_literatura = biologia_literatura(Biologia, literatura)
def biologia_matematica(b,  m):

    return (b & m)

biologia_matematica = biologia_matematica(Biologia, Matematica)

def dos_de_tres(b, m, l):

    return (b &  m & l)






dos_de_tres = dos_de_tres(Biologia, literatura, Matematica)

plt.figure('Primer parcial de Matematica 3 ')

diagram=venn3((1,1,1,1,1,1,1), set_labels=(" Matematica", " Biologia ","literatura"))

for subset in("111","110","101","100","011","010","001"):
    diagram.get_label_by_id(subset).set_text(subset)


diagram.get_label_by_id('100').set_text(sum(sololiteratura))
diagram.get_label_by_id('010').set_text(sum(solobiologia))
diagram.get_label_by_id('001').set_text(sum(solomatematica))
diagram.get_label_by_id('110').set_text(sum(biologia_literatura))
diagram.get_label_by_id('011').set_text(sum(biologia_matematica))
diagram.get_label_by_id('101').set_text(sum(inters_matenatica_literatura))
diagram.get_label_by_id('111').set_text(sum(Biologia_Matematica_Literatura))
 
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1)) # trazo grueso circulo
plt.axis('on')   # Recuadro 
plt.title("Escuela") #  título


plt.show()