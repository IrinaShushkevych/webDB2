from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+psycopg2://postgres:univer@localhost:5432/univer-postgres")

metadata = MetaData()

DBSession = sessionmaker(bind=engine)
session = DBSession()