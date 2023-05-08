from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from distutils.log import debug
from email import message
from sre_constants import SUCCESS
from flask import Flask,render_template,request
from website.api import *
from flask_restful import Api
from website.database import db

app = None
api=None
DB_NAME = "database.db"
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'gughan'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.app_context().push()
    api=Api(app)
    db.init_app(app)
    create_database(app)

    return app,api


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all()

app,api = create_app()


api.add_resource(UserAPI,'/api/user','/api/user/<int:user_id>')
api.add_resource(TicketAPI,'/api/ticket','/api/ticket/<int:ticket_id>')
api.add_resource(AdminAPI,'/api/admin','/api/admin/<int:admin_id>')
api.add_resource(PassengerAPI,'/api/passenger','/api/passenger/<int:passenger_id>')
api.add_resource(FlightAPI,'/api/flight','/api/flight/<int:flight_id>')
api.add_resource(AirportAPI,'/api/airport','/api/airport/<int:airport_id>')

if __name__ == '__main__':
    app.run(debug=True)