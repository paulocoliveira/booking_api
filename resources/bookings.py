from flask_restful import Resource, reqparse
from resources.data import BOOKINGS
import json

class BookingList(Resource):
    # def delete(self):
    #     BOOKINGS.clear()
    #     return BOOKINGS, 204

    def delete(id):
        BOOKINGS.pop(id)
        return BOOKINGS, 204

    def get(self):
        return BOOKINGS, 200
    
    # def get(id):
    #     item = BOOKINGS.get(id)
    #     return item, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("first_name")
        parser.add_argument("last_name")
        parser.add_argument("total_price")
        parser.add_argument("deposit_paid")
        parser.add_argument("checkin")
        parser.add_argument("checkout")
        parser.add_argument("additional_needs")
        args =parser.parse_args()
        if len(BOOKINGS) > 0:
            booking_id = int(max(BOOKINGS.keys())) + 1
        else:
            booking_id = 1
        booking_id = "%i" % booking_id
        BOOKINGS[booking_id] = {
            "first_name": args["first_name"],
            "last_name": args["last_name"],
            "total_price": args["total_price"],
            "deposit_paid": args["deposit_paid"],
            "checkin": args["checkin"],
            "checkout": args["checkout"],
            "additional_needs": args["additional_needs"]
        }
        return BOOKINGS[booking_id], 201