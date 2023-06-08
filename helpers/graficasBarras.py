import matplotlib.pyplot as plt

def graficarsiembra(dataframe, columnaX, columnaY, nombreGrafica):
    
    colores=['green', 'blue', 'red']
    
    siembraPromedio=dataframe.groupby('columnaX')[columnaY].mean()
   
   #plt.bar (siembraPromedio.index ,siembraPromedio,color=colores)
   #plt.xlabel('Numero Arboles') 
   #plt.ylabel('Hectareas')
   #plt.title('Siembra Promedio por Hectarea')
   
   #plt.savefig (f'../assets/img/{nombreGrafica}.png',dpi=300,bbox_inches='tight')
    

