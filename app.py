### crud operations (create, read, update, delete) for the database
from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

##insert data
user = User(name="John Doe", age=30)
user_2 = User(name="Andrew", age=25)
user_3 = User(name="Jane", age=28)
user_4 = User(name="Doe", age=35)

session.add(user_2)
session.add_all([user_3, user_4])


session.add(user)
session.commit()

