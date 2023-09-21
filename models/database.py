from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, CHAR, Date, Float,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import date, datetime


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
    
    # Define a one-to-many relationship from User to Campaign
    campaign_user = relationship('Campaign', back_populates='user_campaign')
    impression_user = relationship('Impression', back_populates='user_impression')
    tag_user = relationship('Tag', back_populates='user_tag')
    
    def __init__(self, first_name, last_name, email, password, date_of_birth, contact_number):
        self.first_name:str = first_name
        self.last_name:str = last_name
        self.email:str = email
        self.password:str = password
        self.date_of_birth:date = date_of_birth
        self.contact_number:str = contact_number
    
    def __repr__(self):
        return f"<User {self.first_name} {self.last_name} {self.email} {self.password} {self.date_of_birth} {self.contact_number}>"





class Campaign(Base):
    __tablename__ = 'campaigns'

    campaign_id = Column(Integer, primary_key=True, autoincrement=True)
    campaign_name = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)  # Assuming FK reference to the 'users' table
    status = Column(String(20), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    budget = Column(Float, nullable=False)

    # Define a relationship with the User entity (assuming you have a User class)
    user_campaign = relationship('User', back_populates='campaign_user')
    ad_group_campaign = relationship('ADGroup', back_populates='campaign_ad_group')

    def __init__(self, campaign_name, user_id, status, start_date, end_date, budget):
        self.campaign_name:str = campaign_name
        self.user_id:int = user_id
        self.status:str= status
        self.start_date:date = start_date
        self.end_date:date = end_date
        self.budget:int = budget

    def __repr__(self):
        return f"<Campaign {self.campaign_name} {self.status} {self.start_date} {self.end_date} {self.budget}>"






class AD(Base):
    __tablename__ = 'ads'

    ad_id = Column(Integer, primary_key=True, autoincrement=True)
    ad_group_id = Column(Integer, ForeignKey('ad_groups.ad_group_id'), nullable=False)
    ad_title = Column(String(100), nullable=False)
    ad_description = Column(String(255), nullable=False)
    status = Column(String(20), nullable=False)
    clickthroughrate = Column(Float, nullable=False)
    
    ad_group_ad = relationship('ADGroup', back_populates='ad_ad_group')
    impression_ad = relationship('Impression', back_populates='ad_impression')

    def __init__(self, ad_group_id, ad_title, ad_description, status, clickthroughrate):
        self.ad_group_id = ad_group_id
        self.ad_title = ad_title
        self.ad_description = ad_description
        self.status = status
        self.clickthroughrate = clickthroughrate

    def __repr__(self):
        return f"<AD {self.ad_title} {self.status} {self.clickthroughrate}>"







class ADGroup(Base):
    __tablename__ = 'ad_groups'

    ad_group_id = Column(Integer, primary_key=True, autoincrement=True)
    campaign_id = Column(Integer, ForeignKey('campaigns.campaign_id'), nullable=False)
    ad_group_name = Column(String(100), nullable=False)
    status = Column(String(20), nullable=False)
    budget = Column(Float, nullable=False)

    # Define a relationship with the Campaign entity
    campaign_ad_group = relationship('Campaign', back_populates='ad_group_campaign')
    ad_ad_group = relationship('AD', back_populates='ad_group_ad')

    def __init__(self, campaign_id, ad_group_name, status, budget):
        self.campaign_id = campaign_id
        self.ad_group_name = ad_group_name
        self.status = status
        self.budget = budget

    def __repr__(self):
        return f"<ADGroup {self.ad_group_name} {self.status} {self.budget}>"








class Impression(Base):
    __tablename__ = 'impressions'

    impression_id = Column(Integer, primary_key=True, autoincrement=True)
    ad_id = Column(Integer, ForeignKey('ads.ad_id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    location = Column(String(100), nullable=False)
    
    user_impression = relationship('User', back_populates='impression_user')
    ad_impression = relationship('AD', back_populates='impression_ad')
    click_impression = relationship('Click', back_populates='impression_click')

    def __init__(self, ad_id, user_id, location):
        self.ad_id = ad_id
        self.user_id = user_id
        self.location = location

    def __repr__(self):
        return f"<Impression {self.timestamp} {self.location}>"





class Click(Base):
    __tablename__ = 'clicks'

    click_id = Column(Integer, primary_key=True, autoincrement=True)
    impression_id = Column(Integer, ForeignKey('impressions.impression_id'), nullable=False)
    time = Column(DateTime, default=datetime.utcnow, nullable=False)
    cost = Column(Float, nullable=False)

    impression_click = relationship('Impression', back_populates='click_impression')
    conversion_click = relationship('Conversion', back_populates='click_conversion')

    def __init__(self, impression_id, cost):
        self.impression_id = impression_id
        self.cost = cost

    def __repr__(self):
        return f"<Click {self.time} {self.cost}>"







class Conversion(Base):
    __tablename__ = 'conversions'

    conversion_id = Column(Integer, primary_key=True, autoincrement=True)
    click_id = Column(Integer, ForeignKey('clicks.click_id'), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    revenue = Column(Float, nullable=False)
    conversion_value = Column(Float, nullable=False)
    
    click_conversion = relationship('Click', back_populates='conversion_click')

    def __init__(self, click_id, revenue, conversion_value):
        self.click_id = click_id
        self.revenue = revenue
        self.conversion_value = conversion_value

    def __repr__(self):
        return f"<Conversion {self.timestamp} {self.revenue} {self.conversion_value}>"
    





class Tag(Base):
    __tablename__ = 'tags'

    tag_id = Column(Integer, primary_key=True, autoincrement=True)
    tag_name = Column(String(100), nullable=False)

    # Define a many-to-one relationship from Tag to User
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    user_tag = relationship('User', back_populates='tag_user')

    def __init__(self, tag_name, user_id):
        self.tag_name = tag_name
        self.user_id = user_id

    def __repr__(self):
        return f"<Tag {self.tag_name}>"    



    
engine = create_engine('sqlite:///database.db', echo=True)    
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
session.commit()
    