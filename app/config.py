# config conexion a base de datos
class Config:
  SECRET_KEY = 'tu_clave_secreta'
  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/crud'
  SQLALCHEMY_TRACK_MODIFICATIONS = False;