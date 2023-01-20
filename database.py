from sqlalchemy.orm import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine=create_engine("postgresql://postgres:Iamraina2001@localhost/kimberlyProject",echo=True)

Base=declarative_base()

SessionLocal= sessionmaker(bind=engine)