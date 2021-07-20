import folium
from folium import IFrame
from folium.plugins import MarkerCluster
import pymongo
import pandas as pd
import IPython
import html
import branca

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["b3"]
coleccion1 = db["archivos"]

centro = [-39.81422, -73.24589]
my_map = folium.Map(location = centro, zoom_start = 14)

#Se ocupa $exists para asegurarme solo lea los documentos que posean el parametro Latitud,
#ya que tengo otros documentos audios insertados los cuales no tienen Latitud.
for doc in db.archivos.find({ "Latitud": { "$exists": "true" } }):
	html = "<p>USUARIO: " +  str(doc['Usuario']['nombre']) + " </p"
	html += "<p>" +  str(doc['Usuario']['apellido']) + " </p <br>"
	html += "<p>Latitud , Longitud: " + "(" + str(doc['Latitud']) + " , " + str(doc['Longitud']) +")" + "</p <br>"
	html += "<p>Formato: " + str(doc['Formato']) + " </p <br>"
	html += "<p>Duracion: " + str(doc['Duracion']) + " segundos" + "</p <br>"
	html += "<p>Fecha Grabacion: " + str(doc['Fecha_Grabacion']) + " </p <br>"
	html += "<p>Exterior o interior: " + str(doc['Exterior_interior']) + " </p <br>"
	html += "<p>Tipo analizador: " + str(doc['Segmentos'][0]['Analizar'][0]['tipo_analizador']) + " </p <br>"
	html += "<p>Categoria: " + str(doc['Segmentos'][0]['Analizar'][0]['categoria']) + " </p <br>"
	html += "<p>Nombre fuente: " + str(doc['Segmentos'][0]['Analizar'][0]['nombre_fuente']) + " </p <br>"
	html += "<p>Descripcion: " + str(doc['Segmentos'][0]['Analizar'][0]['descripcion']) + " </p <br>"
	html += '''
			<audio controls>
  				<source src="ringtone.wav" type="audio/wav" />
			</audio>
			'''
	frame = branca.element.IFrame(html = html, width = 700, height = 390) 
	folium.Marker(location= [ doc['Latitud'], doc['Longitud'] ],popup = folium.Popup(frame, max_width=300),
					icon=folium.Icon(icon_color='green')).add_to(my_map)
	
my_map.save('data.html')


#branca.element.IFrame(html=None, width='100%', height=None, ratio='60%', figsize=None)


from playsound import playsound
from AppKit import NSSound

ARCHIVO_ANIMAL = "vaca.wav"
#playsound(ARCHIVO_ANIMAL)

ARCHIVO_HUMANO = "nino.wav"
#playsound(ARCHIVO_HUMANO)

