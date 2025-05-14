
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


#"<dialect>://<username>:<password>@<host>:<port>/<database>"

# postgresql - use pgadmin4
postgresql_db_url = "postgresql://postgres:password@localhost:5432/postgres"
# mysql - use mysql workbench
mysql_db_url = "mysql+pymysql://root:password@localhost:3306/mysql"
#oracle 
oracle_db_url = "oracle+cx_oracle://username:password@localhost:1521/orcl"
#sqlite
sqlite_db_url = "sqlite:///sqlalchemy_tutorial.db"
# Create an engine instance 

engine = create_engine(sqlite_db_url)

Base = declarative_base()


### creating table 
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    
Base.metadata.create_all(engine)
