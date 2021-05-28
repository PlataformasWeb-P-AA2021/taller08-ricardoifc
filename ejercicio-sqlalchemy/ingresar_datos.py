# importar librerias
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from csv import reader
import csv
# se importa la clase(s) del 
# archivo genera_tablas
from generar_tablas import Fifa

# Base de datos
engine = create_engine('sqlite:///basefifa.db')

Session = sessionmaker(bind=engine)
session = Session()

# Abrir archivo csv
with open("data/mundial2018.csv", "r") as f:
    #agregar en diccionario
    reader = csv.DictReader(f, delimiter='|')
    a = list(reader)
    for d in a:
        # Agregar los datos 
        agregar = Fifa(numero = d['Numero'], fifadisplayName = d['FIFADisplayName'], country = d['Country'], lastName = d['LastName'], firstName = d['FirstName'],
        shirtName = d['ShirtName'], pos = d['POS'], height = d['Height'], caps = d['Caps'], goals = d['Goals'])
        session.add(agregar)

# agregar a la BD
session.commit()
