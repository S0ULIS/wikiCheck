# *-* utf-8 *-*
from collections import namedtuple
import wikipedia
import csv

keywords = ["Matemático","matemático","Matemática","matemática","teorema","matematico","Matematico","matematica","Matematica", "Teorema","mathematician","Mathematician"]
wikipedia.set_lang("es")

# Filenames

fichIn = "vial_Sevilla_Bueno.csv"
fichOut = "matematicos.csv"



verbose = False
Calle = namedtuple("Calle", "calle,municipio,nombre,x,y")

def get_offset():
    try:
        with open("offset.txt") as f:
            offset = int(f.read())
    except:
        offset = 0
    return offset

def set_offset(new_offset=-1):
    if new_offset>=0:
        with open("offset.txt","w") as f:
            f.write(str(new_offset))

def lee_calles(fichero,offset=0):
    result = []
    with open(fichero,encoding="Latin1") as f:
        lector = csv.reader(f,delimiter=";")
        next(lector)
        for i in range(offset-1):
            next(lector)
        for linea in lector:
            result.append(Calle(linea[11],linea[8],linea[5],linea[9],linea[10]))
    return result

def is_mathematician(calle,keywords):
    result = False
    try:
        pagina = wikipedia.page(calle.nombre)
        for key in keywords:
            if key in pagina.content:
                result=True
    except wikipedia.exceptions.DisambiguationError as e:
        print("Más de un resultado disponible")
        if verbose:
            print(e)
    except wikipedia.exceptions.PageError:
        print("Página no encontrada")
    return result

def anadir_calle(calle):
    with open(fichOut,"a", encoding="Latin1") as f:
        f.write("{},{},{},{},{}\n".format(calle.calle,calle.municipio,calle.nombre,calle.x,calle.y))

def restart_files():
    with open(fichOut,"w", encoding="Latin1") as f:
        f.write("patrocinado,por,mapamático,:),:)\n")
    with open("offset.txt","w") as f:
        f.write("0")
    

if __name__=="__main__":
    try:
        opt = int(input("Introduzca 1 para seguir desde donde lo dejó o 2 para empezar de nuevo: "))
    except:
        print("Opción no válida")
    if(opt==2):
        restart_files()
    offset = get_offset()    
    calles = lee_calles(fichIn,offset)
    total = len(calles)
    print("Comenzando por {} de un total de {}".format(offset,total+offset))
    for calle in calles:
        print("[+] Analizando: {}. {}%".format(calle.calle,round(offset*100/(total+offset),2)))
        if is_mathematician(calle,keywords):
            print("[+] Nueva calle encontrada: {}".format(calle.calle))
            anadir_calle(calle)
        offset+=1
        set_offset(offset)

