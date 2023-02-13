from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

username = 'postgres'
password = 'Dctjabutyyj100geljd'
host = '127.0.0.1'
port = '5432'
db_name = 'postgres'

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


if __name__ == "__main__":
    Base.metadata.create_all(engine)


#docker run --name my_db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=Dctjabutyyj100geljd -p 5432:5432 -d postgres