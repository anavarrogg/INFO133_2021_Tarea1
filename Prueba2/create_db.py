import pymongo
import gridfs
from bson import ObjectId
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

db = myclient["b3"]

coleccion1 = db["archivos"]
coleccion2 = db["Fuente"]

coleccion1.insert_many([
			{
				"Usuario": {
						"rut": "18173558-9", 
						"nombre": "Julian", 
						"apellido": "Fernandez" 
						},
				"id_archivo": 1,
				"dato": {# lista de _id que hace 
				#referencia a diferentes audios que este usuario usa
						"audio1": ObjectId("60f72dde97fe53498072e5ba"),
						"audio2": ObjectId("60f72dde97fe53498072e5bb")
						},
				"Fecha_Grabacion": "22-05-2021",
				"Ciudad": "Valdivia",
				"Formato": "wav",
				"Duracion": 18,
				"Exterior_interior": "interior",
				"Latitud": -39.81422,
				"Longitud": -73.24589,
				"Segmentos": [{
						"id_segmento": 1,
						"formato": "wav",
						"Duracion": 18,
						"inicio": 0,
						"fin": 18,
						"Analizar": [{
								"tipo_analizador": "Computador",
								"descripcion": "Ringtone",
								"nombre_fuente": "Cancion",
								"porcentaje": None,
								"categoria": "Musica"
							}]
				}]
			},
			{
				"Usuario": {
						"rut": "1888558-9", 
						"nombre": "Alexis", 
						"apellido": "Sanchez" 
						},
				"id_archivo": 2,
				"dato": {# lista de _id que hace 
				#referencia a diferentes audios que este usuario usa
						"audio1": ObjectId("60f72dde97fe53498072e5bc"),
						"audio2": ObjectId("60f72dde97fe53498072e5bb"),
						"audio3": ObjectId("60f72dde97fe53498072e5ba")
						},
				"Fecha_Grabacion": "22-05-2021",
				"Ciudad": "Valdivia",
				"Formato": "wav",
				"Duracion": 3,
				"Exterior_interior": "interior",
				"Latitud": -39.82422,
				"Longitud": -73.24589,
				"Segmentos": [{
						"id_segmento": 1,
						"formato": "wav",
						"Duracion": 3,
						"inicio": 0,
						"fin": 3,
						"Analizar": [{
								"tipo_analizador": "Humano",
								"descripcion": "Hablar",
								"nombre_fuente": "Bebe",
								"porcentaje": 70,
								"categoria": "Humano"							
							}]
				}]
			},
			{
				"Usuario": {
						"rut": "2088558-9", 
						"nombre": "Jorge", 
						"apellido": "Valdivia" 
						},
				"id_archivo": 3,
				"dato": {# lista de _id que hace 
				#referencia a diferentes audios que este usuario usa
						"audio1": ObjectId("60f72dde97fe53498072e5bc"),
						"audio2": ObjectId("60f72dde97fe53498072e5bb")
						},
				"Fecha_Grabacion": "22-05-2021",
				"Ciudad": "Valdivia",
				"Formato": "wav",
				"Duracion": 3,
				"Exterior_interior": "exterior",
				"Latitud": -39.83422,
				"Longitud": -73.25589,
				"Segmentos": [{
						"id_segmento": 1,
						"formato": "wav",
						"Duracion": 3,
						"inicio": 0,
						"fin": 3,
						"Analizar": [{
								"tipo_analizador": "Humano",
								"descripcion": "Mugido",
								"nombre_fuente": "Vaca",
								"porcentaje": 70,
								"categoria": "Animales"							
							}]
				}]			
			},
			{
				"Usuario": {
						"rut": "3088558-9", 
						"nombre": "Martin", 
						"apellido": "Isla" 
						},
				"id_archivo": 4,
				"dato": {# lista de _id que hace 
				#referencia a diferentes audios que este usuario usa
						"audio1": ObjectId("60f72dde97fe53498072e5ba"),
						"audio2": ObjectId("60f72dde97fe53498072e5bb")
						},
				"Fecha_Grabacion": "22-05-2021",
				"Ciudad": "Valdivia",
				"Formato": "wav",
				"Duracion": 3,
				"Exterior_interior": "exterior",
				"Latitud": -39.84422,
				"Longitud": -73.23639,
				"Segmentos": [{
						"id_segmento": 1,
						"formato": "wav",
						"Duracion": 3,
						"inicio": 0,
						"fin": 3,
						"Analizar": [{
								"tipo_analizador": "Computador",
								"descripcion": "Mugido",
								"nombre_fuente": "Vaca",
								"porcentaje": None,
								"categoria": "Animales"
							}]


				}]			
			},
			{
				"Usuario": {
						"rut": "4088558-9", 
						"nombre": "Eduardo", 
						"apellido": "Vargas" 
						},
				"id_archivo": 5,
				"dato": {# lista de _id que hace 
				#referencia a diferentes audios que este usuario usa
						"audio1": ObjectId("60f72dde97fe53498072e5bc"),
						"audio2": ObjectId("60f72dde97fe53498072e5bb"),
						"audio3": ObjectId("60f72dde97fe53498072e5ba")
						},
				"Fecha_Grabacion": "22-05-2021",
				"Ciudad": "Valdivia",
				"Formato": "wav",
				"Duracion": 18,
				"Exterior_interior": "interior",
				"Latitud": -39.85422,
				"Longitud": -73.22639,
				"Segmentos": [{
						"id_segmento": 1,
						"formato": "wav",
						"Duracion": 18,
						"inicio": 0,
						"fin": 18,
						"Analizar": [{
								"tipo_analizador": "Humano",
								"descripcion": "Ringtone",
								"nombre_fuente": "Cancion",
								"porcentaje": 70,
								"categoria": "Musica"							
							}]

				}]			
			}

		])
			


#x = coleccion1.insert_one(archivos)

#print("Lista de colecciones: \n--------------------")
#for coll in mydb.list_collection_names():
#   print(coll)
