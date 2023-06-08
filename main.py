import pandas as pd
from data.datos1 import tabla
from helpers.crearTablasHtml import crearTabla
#from helpers.graficasBarras import graficarPromedioSiembra
from helpers.graficastorta import graficar_torta

#- FILTRO1: Encontrar todos los datos de santa fe de Antioquia donde se tengan siembras de + de 250 arboles
santaFe=tabla.query('(Ciudad=="Santa Fe de Antioquia")&(Arboles>=250)')
#print(santaFe)

#- FILTRO2: Filtrar todos los datos de Caucasia e interpretar sus estadísticas
caucasia=tabla.query('Ciudad=="Caucasia"')
#print(caucasia)

#- FILTRO 3: Filtrar todos los datos de las veredas Rio arriba y la Salazar de Belmira
belmira=tabla.query('(Vereda=="Rio Arriba")|(Vereda=="La Salazar")')
#print(belmira)


#- FILTRO 4: Encontrar los datos de las veredas Quitasol de Bello mostrando además las medias de cada ítem del dataframe
bello=tabla.query('(Ciudad=="Bello")&(Vereda=="Quitasol")')
#print(bello)

#- FILTRO 5: Encontrar todos los datos de caramanta donde se tengan siembras de + de 100 arboles
caramanta=tabla.query('(Ciudad=="Caramanta")&(Arboles>100)')
#print(caramanta)

#- FILTRO 6: Encontrar los datos de la vereda mallarino del municipio de Yarumal
yarumal=tabla.query('(Ciudad=="Yarumal")&(Vereda=="Mallarino")')
#print(yarumal)

#Genereal de cada municipio
gnralYarumal=tabla.query('Ciudad=="Yarumal"')
gnralSantafe=tabla.query('Ciudad=="Santa Fe de Antioquia"')
gnralCaucasia=tabla.query('Ciudad=="Caucasia"')
gnralBelmira=tabla.query('Ciudad=="Belmira"')
gnralBello=tabla.query('Ciudad=="Bello"')
gnralCaramanta=tabla.query('Ciudad=="Caramanta"')

#Creando tablas

crearTabla(santaFe,"arbolesStafe")
crearTabla(caucasia,"estadisticaCaucasia")
crearTabla(belmira,"veredasBelmira")
crearTabla(bello,"veredasBello")
crearTabla(caramanta,"arbolesCaramanta")
crearTabla(yarumal,"veredasYarumal")
crearTabla(tabla,"generalAnt")
crearTabla(gnralBello,"generalBello")
crearTabla(gnralBelmira,"generalBelmira")
crearTabla(gnralCaramanta,"generalCaramanta")
crearTabla(gnralYarumal,"generalYarumal")
crearTabla(gnralSantafe,"generalSantafe")
crearTabla(gnralCaucasia,"generalCaucasia")

#Generamos graficas
#graficarPromedioSiembra(tabla, 'Arboles','Hectareas','PromedioSiembra')
graficar_torta(caramanta, [300, 800, 1300, 1800, 2300, 2800, 3200], 'Arboles', 'Hectareas', 'datosCaramanta')