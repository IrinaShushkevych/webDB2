# docker run --name univer-postgres -p 5432:5432 -e POSTGRES_PASSWORD=univer -d postgres
import models
import connect

models.Base.metadata.create_all(connect.engine)
models.Base.metadata.bind = connect.engine