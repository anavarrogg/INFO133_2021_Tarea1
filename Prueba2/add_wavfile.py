from bson.binary import Binary
from bson import ObjectId
import pymongo, gridfs
from gridfs import GridFS
from pymongo import MongoClient
import base64

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["b3"]
coleccion1 = db["archivos"]

# Primero se codifican los 3 audios a base 64, despues se crea un archivo temporal en formato wav
# en el cual se escribe la decodificacion de string base64, de esta forma se ve mucho mas simplificado al hacer db.archivos.find().pretty()

encode_musica = base64.b64encode(open("ringtone.wav", "rb").read())
model_file1 = open("temp1.wav", "wb")
decode_string1 = base64.b64decode(encode_musica)
x1 = model_file1.write(decode_string1)
coleccion1.insert_one({"file": x1, "descripcion": "Audio Ringtone" })

encode_humano = base64.b64encode(open("nino.wav", "rb").read())
model_file2 = open("temp2.wav", "wb")		
decode_string2 = base64.b64decode(encode_humano)
x2 = model_file2.write(decode_string2)
coleccion1.insert_one({"file": x2, "descripcion": "Audio Bebe" })

encode_animal = base64.b64encode(open("vaca.wav", "rb").read())
model_file3 = open("temp3.wav", "wb")
decode_string3 = base64.b64decode(encode_animal)
x3 = model_file3.write(decode_string3)
coleccion1.insert_one({"file": x3, "descripcion": "Audio Vaca" })
