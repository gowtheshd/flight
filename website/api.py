from flask_restful import Resource, fields, marshal_with, reqparse, marshal
from website.models import *
from sqlalchemy import and_
from flask import make_response,jsonify
from website.database import db
from  werkzeug.exceptions import HTTPException



class Error(HTTPException):
    def __init__(self, status_code,err_code,error_message):
        message={"error_code":err_code,"error_message":error_message,"status":status_code}
        self.response=make_response(jsonify(message),status_code)    
        
        
user_fields = {
    'id': fields.Integer,
    'email':fields.String,
    'username': fields.String,
    'phone':fields.Integer,
    'password': fields.String
}

ticket_fields={
    'user_id':fields.Integer,
    'flight_id':fields.Integer,
    'passenger_id':fields.Integer
}

admin_fields={
    'password':fields.String,
    'username':fields.String
}

passenger_fields={
    'gender':fields.String,
    'age':fields.Integer,
    'username':fields.String,
    'adhaarnumber':fields.Integer
}

airport_fields={
    'name':fields.String,
    'address':fields.String,
    'city':fields.String,
    'pincode':fields.Integer
}

flight_fields={
    'flightno':fields.Integer,
    'frm':fields.Integer,
    'date':fields.String,
    'charge':fields.Integer,
    'to':fields.Integer,
    'available_seat':fields.Integer
}

search_fields={
    
}

create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument('username')
create_user_parser.add_argument('email')
create_user_parser.add_argument('password')
create_user_parser.add_argument('phone')

edit_user_parser =reqparse.RequestParser()
edit_user_parser.add_argument('username')
edit_user_parser.add_argument('phone')

create_ticket_parser =reqparse.RequestParser()
create_ticket_parser.add_argument('user_id')
create_ticket_parser.add_argument('passenger_id')
create_ticket_parser.add_argument('flight_id')

create_admin_parser = reqparse.RequestParser()
create_admin_parser.add_argument('username')
create_admin_parser.add_argument('password')

create_passenger_parser = reqparse.RequestParser()
create_passenger_parser.add_argument('username')
create_passenger_parser.add_argument('age')
create_passenger_parser.add_argument('gender')
create_passenger_parser.add_argument('adhaarnumber')

edit_passenger_parser = reqparse.RequestParser()
edit_passenger_parser.add_argument('age')
edit_passenger_parser.add_argument('gender')


create_flight_parser=reqparse.RequestParser()
create_flight_parser.add_argument('flightno')
create_flight_parser.add_argument('frm')
create_flight_parser.add_argument('date')
create_flight_parser.add_argument('charge')
create_flight_parser.add_argument('to')

edit_flight_parser=reqparse.RequestParser()
edit_flight_parser.add_argument('date')
edit_flight_parser.add_argument('frm')
edit_flight_parser.add_argument('to')
edit_flight_parser.add_argument('charge')

create_airport_parser=reqparse.RequestParser()
create_airport_parser.add_argument('name')
create_airport_parser.add_argument('address')
create_airport_parser.add_argument('city')
create_airport_parser.add_argument('pincode')

edit_airport_parser=reqparse.RequestParser()
edit_airport_parser.add_argument('city')
edit_airport_parser.add_argument('pincode')




class UserAPI(Resource):
    
    @marshal_with(user_fields)
    def get(self, user_id):
        user=User.query.filter(User.id == user_id).first()
        if user:
            return user
        else:
            raise Error(400,"USER_DOES_NOT_EXIST","User not found")
    
    @marshal_with(user_fields)
    def post(self):
        args = create_user_parser.parse_args()
        email = args.get("email", None)
        password = args.get("password", None)
        username = args.get("username", None)
        phone = args.get("phone", None)
        exist = User.query.filter(User.email == email).first()  
        exist2 = User.query.filter(User.username == username).first()
        if exist:
            raise Error(400,"EMAIL_ALREADY_EXISTS","Email Already Exists")
        elif exist2:
            raise Error(400,"USERNAME_ALREADY_EXISTS","Username already exists")
        else:
            user = User(email=email, password=password, username=username, phone=phone )
            db.session.add(user)
            db.session.commit()

        return user
    
    @marshal_with(user_fields)
    def put(self, user_id):
        args = edit_user_parser.parse_args()
        username = args.get("username", None)
        phone = args.get("phone", None)
        #check_username(username_
        user = User.query.filter(User.username == username).first()
        if user:
            raise Error(400,"USERNAME_ALREADY_EXISTS","Username Already Exists")
        user=User.query.filter(User.id == user_id).first()
        user.username = username
        user.phone = phone
        db.session.add(user)
        db.session.commit()

        return user
    
    def delete(self, user_id):
        user=User.query.filter(User.id == user_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return {"msg" : "User Deleted"}, 200
        else:
            raise Error(400,"USER_DOES_NOT_EXIST","User not found")






class TicketAPI(Resource):
    @marshal_with(ticket_fields)
    def get(self, ticket_id):
        ticket=Ticket.query.filter(Ticket.id==ticket_id).first()
        if ticket:
            return ticket
        else:
            raise Error(400,"USER_DOES_NOT_EXIST","User not found")
    
    @marshal_with(ticket_fields)
    def post(self):
        args = create_ticket_parser.parse_args()
        user_id = args.get("user_id", None)
        flight_id = args.get("flight_id", None)
        passenger_id = args.get("passenger_id", None)
        flight=Flight.query.filter(Flight.id==flight_id).first()
        if flight.available_seat==0:
            raise Error(400,"TICKETS_ARE_FULL","Tickets are full")
        else:
            ticket = Ticket(user_id=user_id,flight_id=flight_id,passenger_id=passenger_id)
            db.session.add(ticket)
            db.session.commit()
            count=flight.available_seat
            count=-1
            flight.available_seat=count
            db.session.commit()

        return ticket
   
   
   
   
   
   
    
class AdminAPI(Resource):
    @marshal_with(admin_fields)
    def get(self, admin_id):
        admin=Admin.query.filter(Admin.id == admin_id).first()
        if admin:
            return admin
        else:
            raise Error(400,"USER_DOES_NOT_EXIST","User not found")
    
    @marshal_with(admin_fields)
    def post(self):
        args = create_admin_parser.parse_args()
        password = args.get("password", None)
        username = args.get("username", None)
        exist = Admin.query.filter(Admin.username == username).first()
        if exist:
            raise Error(400,"EMAIL_ALREADY_EXISTS","Email Already Exists")
        else:
            admin = Admin(password=password, username=username)
            db.session.add(admin)
            db.session.commit()

        return admin
    
    def delete(self, admin_id):
        admin=Admin.query.filter(Admin.id == admin_id).first()
        if admin:
            db.session.delete(admin)
            db.session.commit()
            return {"msg" : "User Deleted"}, 200
        else:
            raise Error(400,"USER_DOES_NOT_EXIST","User not found")
 
 
 
 
 
 
class PassengerAPI(Resource):
    
    @marshal_with(passenger_fields)
    def get(self, passenger_id):
        passenger=Passenger.query.filter(Passenger.id == passenger_id).first()
        if passenger:
            return passenger
        else:
            raise Error(400,"USER_DOES_NOT_EXIST","User not found")
    
    @marshal_with(passenger_fields)
    def post(self):
        args = create_passenger_parser.parse_args()
        gender = args.get("gender", None)
        age = args.get("age", None)
        username = args.get("username", None)
        adhaarnumber = args.get("adhaarnumber", None)
        exist = Passenger.query.filter(Passenger.adhaarnumber== adhaarnumber).first()
        if exist:
            raise Error(400,"ADHAARNUMBER_IS_SAME","Same adhaar number!!!")
        else:
            passenger = Passenger(gender=gender, adhaarnumber=adhaarnumber, username=username, age=age )
            db.session.add(passenger)
            db.session.commit()

        return passenger
    def delete(self, passenger_id):
        passenger=Passenger.query.filter(Passenger.id == passenger_id).first()
        if passenger:
            db.session.delete(passenger)
            db.session.commit()
            return {"msg" : "User Deleted"}, 200
        else:
            raise Error(400,"USER_DOES_NOT_EXIST","User not found")
    
    @marshal_with(passenger_fields)
    def put(self, passenger_id):
        args = edit_passenger_parser.parse_args()
        age = args.get("age", None)
        gender = args.get("gender", None)
        passenger=Passenger.query.filter(Passenger.id == passenger_id).first()
        passenger.age = age
        passenger.gender = gender
        db.session.add(passenger)
        db.session.commit()

        return passenger
    
    
    
    
    
class FlightAPI(Resource):
    @marshal_with(flight_fields)
    def get(self, flight_id):
        flight=Flight.query.filter(Flight.id == flight_id).first()
        if flight:
            return flight
        else:
            raise Error(400,"FLIGHT_DOES_NOT_EXIST","Flight not found")
        
    @marshal_with(flight_fields)
    def post(self):
        args = create_flight_parser.parse_args()
        flightno = args.get("flightno", None)
        frm = args.get("frm", None)
        to=args.get("to", None)
        date = args.get("date", None)
        charge = args.get("charge", None)
        exist = Flight.query.filter(and_(Flight.flightno == flightno,Flight.date==date)).first()
        if exist:
            raise Error(400,"FLIGHT_ALREDY_EXISTS_OR_DATE_ARE_SAME","Flight already Exists or date are same")
        else:
            flight = Flight(flightno=flightno, date=date, charge=charge, frm = frm, to=to)
            db.session.add(flight)
            db.session.commit()

        return flight
    
    @marshal_with(flight_fields)
    def put(self, flight_id):
        args = edit_flight_parser.parse_args()
        frm = args.get('frm',None)
        to = args.get("to", None)
        date=args.get("date",None)
        charge=args.get("charge",None)
        #check_username(username_
        exist = Flight.query.filter(and_(Flight.id == flight_id,Flight.date==date)).first()
        if exist:
            raise Error(400,"DATE_ALREADY_EXISTS","Date Already Exists")
        flight=Flight.query.filter(Flight.id == flight_id).first()
        flight.frm = frm
        flight.to = to
        flight.date = date
        flight.charge=charge
        db.session.add(flight)
        db.session.commit()

        return flight

    @marshal_with(flight_fields)    
    def delete(self, flight_id):
        flight=Flight.query.filter(Flight.id == flight_id).first()
        if flight:
            db.session.delete(flight)
            db.session.commit()
            return {"msg" : "User Deleted"}, 200
        else:
            raise Error(400,"USER_DOES_NOT_EXIST","User not found")
    
    



class AirportAPI(Resource):
    @marshal_with(airport_fields)
    def get(self, airport_id):
        airport=Airport.query.filter(Airport.id == airport_id).first()
        if airport:
            return airport
        else:
            raise Error(400,"FLIGHT_DOES_NOT_EXIST","Flight not found")
        
    @marshal_with(airport_fields)
    def post(self):
        args = create_airport_parser.parse_args()
        name = args.get("name", None)
        address=args.get("address", None)
        city = args.get("city", None)
        pincode = args.get("pincode", None)
        exist = Airport.query.filter(Airport.city == city).first()  
        exist1 =Airport.query.filter(Airport.pincode == pincode).first()
        if exist:
            raise Error(400,"CITY_ALREDY_EXISTS","City already Exists are same")
        elif exist1:
            raise Error(400,"PINCODE_ALREDY_EXISTS","Pincode already Exists are same")
        else:
            airport = Airport(name=name, city=city, pincode=pincode,address=address)
            db.session.add(airport)
            db.session.commit()

        return airport
    
    @marshal_with(airport_fields)
    def put(self, airport_id):
        args = edit_airport_parser.parse_args()
        city = args.get("city", None)
        pincode = args.get("pincode", None)
        #check_username(username_
        exist = Airport.query.filter(Airport.city == city).first()
        exist1 =Airport.query.filter(Airport.pincode == pincode).first()
        if exist:
            raise Error(400,"CITY_ALREDY_EXISTS","City already Exists are same")
        elif exist1:
            raise Error(400,"PINCODE_ALREDY_EXISTS","Pincode already Exists are same")
        airport=Airport.query.filter(Airport.id == airport_id).first()
        airport.city=city
        airport.pincode=pincode
        db.session.add(airport)
        db.session.commit()

        return airport

    @marshal_with(airport_fields)    
    def delete(self, airport_id):
        airport=Airport.query.filter(Airport.id == airport_id).first()
        if airport:
            db.session.delete(airport)
            db.session.commit()
            return {"msg" : "User Deleted"}, 200
        else:
            raise Error(400,"USER_DOES_NOT_EXIST","User not found")