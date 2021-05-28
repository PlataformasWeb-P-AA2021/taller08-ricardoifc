from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_tablas
from generar_tablas import Fifa 

# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite

engine = create_engine('sqlite:///basefifa.db')


Session = sessionmaker(bind=engine)
session = Session()

# Obtener todos los registros ordenados
fifaGoals = session.query(Fifa).order_by(Fifa.goals.desc()).all()

# repetitivo for en python
print("presentar todos los jugadores, ordenados por el número de goles")
for p in fifaGoals:
    print("Nombre de Jugador: %s Goles: %d" % (p.fifadisplayName, p.goals))
