import csv
import json
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


def lee_json(fichero):
    result = []
    with open(fichero,"r",encoding="Latin1") as f:
        lector = f.readlines()
        for linea in lector:
            data = linea.split(",")
            result.append(data)

    return result


if __name__=="__main__":
    locator = Nominatim(user_agent="myGeocoder")
    data = lee_json("filtracion.csv")
    manuales = 0
    for calle in data:
        print("{}, {}, Seville, Spain".format(calle[2] if calle[-1]=="" else calle[3],calle[1] if calle[-1]=="" else calle[2]+" "+calle[1]))
        location = locator.geocode("{}, {}, Seville, Spain".format(calle[2] if calle[-1]=="" else calle[3],calle[1] if calle[-1]=="" else calle[2]+" "+calle[1]))
        if location==None:
            print("Nulo")
            calle.append(0.)
            manuales+=1
            calle.append(0.)
        else:
            print("{}, {}".format(location.latitude,location.longitude))
            calle.append(location.latitude)
            calle.append(location.longitude)
    print("{} no encontradas".format(manuales))
    keys = "Nombre,Municipio,articulo,NombreMayus,Url,latitude,longitude".split(",")
    with open("coordenadas.json","w",encoding="Latin1") as f:
        text = "[ \n"

        for calle in data:
            text+="{\n"
            for i in range(len(calle)):
                text+='"{}":"{}",'.format(keys[i],str(calle[i]).replace("\n",""))
            text=text[:-1]
            text+="},"
        text=text[:-1]
        text+="]"
        f.write(text)


    
