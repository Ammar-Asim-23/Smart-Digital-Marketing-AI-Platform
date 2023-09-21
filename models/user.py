from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, CHAR, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column("user_id", Integer, primary_key=True,autoincrement=True)
    first_name = Column("first_name", String(80), nullable=False)
    last_name = Column("last_name", String(80))
    email = Column("email", String(255), unique=True, nullable=False)
    password = Column("password", CHAR(80), nullable=False)
    date_of_birth = Column('date_of_birth', Date, nullable=False)
    contact_number = Column('contact_number', String(20))
    
    def __init__(self, first_name, last_name, email, password, date_of_birth, contact_number):
        self.first_name:str = first_name
        self.last_name:str = last_name
        self.email:str = email
        self.password:str = password
        self.date_of_birth:date = date_of_birth
        self.contact_number:str = contact_number
    
    def __repr__(self):
        return f"<User {self.first_name} {self.last_name} {self.email} {self.password} {self.date_of_birth} {self.contact_number}>"
    
engine = create_engine('sqlite:///database.db', echo=True)    
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

user = User('Abdul', 'Bari', 'abdulbari069@gmail.com', 'Pakistan456', date(2003,7,14), '0301-1234567')

session.add(user)
session.commit()
    