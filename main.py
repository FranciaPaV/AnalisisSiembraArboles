import pandas as pd



#obtenemos los datos de la DB
tabla = pd.read_csv('./data/Siembras.csv')
#print(tabla)

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