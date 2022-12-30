from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:univer@localhost:5401/univer")
# engine = create_engine("postgresql+psycopg2://postgres:univer@192.168.99.100:5401/univer")

metadata = MetaData()

DBSession = sessionmaker(bind=engine)
session = DBSession()