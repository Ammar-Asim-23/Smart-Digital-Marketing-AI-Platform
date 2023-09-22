from markify import db, app
from sqlalchemy import Column, Integer, String, CHAR, Date, Float

class User(db.Model):
    __tablename__ = 'users'
    
    user_id = Column("user_id", Integer, primary_key=True,autoincrement=True)
    firstname = Column("first_name", String(80), nullable=False)
    lastname = Column("last_name", String(80))
    email = Column("email", String(255), unique=True, nullable=False)
    password = Column("password", CHAR(180), nullable=False)
    dateOfBirth = Column('date_of_birth', Date, nullable=False)
    contactno = Column('contact_number', String(20))
    
    def __repr__(self):
        return f"<User {self.first_name} {self.last_name} {self.email} {self.password} {self.date_of_birth} {self.contact_number}>"



with app.app_context():
    db.create_all()