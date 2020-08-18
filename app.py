from flask import Flask
from flask_restful import Resource, Api
from resources.bookings import BookingList, Booking

app = Flask(__name__)
api = Api(app)
app.config['DEBUG'] = True

api.add_resource(BookingList, "/bookings")
api.add_resource(Booking, "/booking", endpoint="post")
api.add_resource(Booking, "/booking/<string:first_name>")

app.run()
