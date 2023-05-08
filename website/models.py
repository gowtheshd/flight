from website.database import db
import datetime

class User(db.Model):
    __tablename__ = 'user'
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150),unique=True,nullable=False)
    email=db.Column(db.String(150),unique=True,nullable=False)
    phone = db.Column(db.Integer,nullable=False)
    password = db.Column(db.String(150),nullable=False)
    
class Flight(db.Model):
    __tablename__ = 'flight'
    id =db.Column(db.Integer, primary_key=True)
    flightno=db.Column(db.Integer,nullable=False)
    frm = db.Column(db.Integer,db.ForeignKey('airport.id'),nullable=False)
    to=db.Column(db.Integer,db.ForeignKey('airport.id'),nullable=False)
    date = db.Column(db.String(120),nullable=False)
    charge = db.Column(db.Integer,nullable=False)
    available_seat = db.Column(db.Integer,default=60,nullable=False)

class Admin(db.Model):
    __tablename__ = 'admin'
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150),unique=True,nullable=False)
    password = db.Column(db.String(150),nullable=False)
    
class Airport(db.Model):
    __tablename__ = 'airport'
    id =db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(150),nullable=False)
    address=db.Column(db.String(150),nullable=False)
    city=db.Column(db.String(150),nullable=False)
    pincode=db.Column(db.Integer,nullable=False)
    
class Ticket(db.Model):
    __tablename__ = 'tickets'
    id =db.Column(db.Integer,primary_key=True,nullable=False)
    flight_id = db.Column(db.Integer,db.ForeignKey('flight.id'),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    passenger_id = db.Column(db.Integer,db.ForeignKey('passenger.id'),nullable=False)
    
class Passenger(db.Model):
    __tablename__ = 'passenger'
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150),unique=True,nullable=False)
    gender=db.Column(db.String(150),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    adhaarnumber=db.Column(db.Integer,nullable=False)