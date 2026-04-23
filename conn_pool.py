from sqlalchemy import create_engine,MetaData

URL='mysql+mysqlconnector://root:pnavyasarada@localhost:3306/sqlalchemy'

engine=create_engine(URL,echo=True)

metadata=MetaData()