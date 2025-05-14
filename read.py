### crud operations (create, read, update, delete) for the database

# Read data from the database
from models import User, engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

users = session.query(User).all()
print(users)

users_2 = users[2]

print(users_2)

print(users_2.id)
print(users_2.name)
print(users_2.age)

#getting as list
for user in users:
    print(f"User id: {user.id}, name:  {user.name}, age : {user.age}")

#filtering
users_3 = session.query(User).filter_by(name="John Doe").all()
print(users_3)

user_4 = session.query(User).filter_by(id=4).one_or_none()
print(user_4)

#changing data
user_4.name = "rahul"
print(user_4.name)
session.commit()

user_5 = session.query(User).filter_by(id=5).one_or_none()
print("Deleting : ", user_5.name)
session.delete(user_5)

session.commit()