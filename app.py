from flask import Flask
from flask_restful import Resource, Api
from resources.bookings import BookingList

app = Flask(__name__)
api = Api(app)

if __name__ == "__main__":
    app.run(port=5000)

api.add_resource(BookingList, "/booking/")