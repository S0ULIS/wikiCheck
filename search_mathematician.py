# *-* utf-8 *-*
from collections import namedtuple
import wikipedia
import csv

keywords = ["Matemático","matemático","Matemática","matemática","teorema","matematico","Matematico", "Teorema"]
wikipedia.set_lang("es")



Calle = namedtuple("Calle", "calle,municipio,nombre")

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
    with open("vialSevillaFiltrado.csv", encoding="Latin1") as f:
        lector = csv.reader(f)
        for i in range(offset-1):
            next(lector)
        for linea in lector:
            result.append(Calle(linea[0],linea[1],linea[2]))
    return result

def is_mathematician(calle,keywords):
    result = False
    try:
        pagina = wikipedia.page(calle.nombre)
        for key in keywords:
            if key in pagina.content:
                result=True
    except wikipedia.exceptions.DisambiguationError as e:
        print("Mas de un resultado disponible")
        print(e)
    except wikipedia.exceptions.PageError:
        print("Página no encontrada")
    return result

def anadir_calle(calle):
    with open("matematicos.csv","a",encoding="Latin1") as f:
        f.write("{},{},{}\n".format(calle.calle,calle.municipio,calle.nombre))
    

if __name__=="__main__":
    
    offset = get_offset()    
    calles = lee_calles("vialSevillaFiltrado.csv",offset)
    total = len(calles)
    print("Comenzando por {} de un total de {}".format(offset,total+offset))
    for calle in calles:
        print("[+] Analizando: {}. {}%".format(calle.calle,round(offset*100/(total+offset),2)))
        if is_mathematician(calle,keywords):
            print("[+] Nueva calle encontrada: {}".format(calle.calle))
            anadir_calle(calle)
        offset+=1
        set_offset(offset)

