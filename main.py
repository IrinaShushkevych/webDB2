# docker run --name univer --restart always -p 5401:5432 -e POSTGRES_PASSWORD=univer -e POSTGRES_DB=univer -d postgres
from . import connect



def main():
    pass

if __name__ == '__main__':
    main()