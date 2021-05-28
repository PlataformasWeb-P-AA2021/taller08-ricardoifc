# importar librerias
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///basefifa.db')
Base = declarative_base()

# Crear la tabla de provincias
class Fifa(Base):
    __tablename__ = 'fifa'
    id = Column(Integer, primary_key=True)
    numero = Column(String(50))
    fifadisplayName = Column(String(40))
    country = Column(String(40))
    lastName = Column(String(40))
    firstName = Column(String(40))
    shirtName = Column(String(40))
    pos = Column(String(40))
    height = Column(Integer)
    caps = Column(Integer)
    goals = Column(Integer)

    
    def __repr__(self):
        return "Fifa: numero=%s FIFADisplayName=%s country=%s lastName=%s firstName=%s shirtName=%s POS=%s height=%d caps=%d goals=%d" % (
                          self.numero,
                          self.fifadisplayName,
                          self.country,
                          self.lastName,
                          self.firstName,
                          self.shirtName,
                          self.pos,
                          self.height,
                          self.caps, 
                          self.goals)

Base.metadata.create_all(engine)