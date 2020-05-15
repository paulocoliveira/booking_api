from flask_restful import Resource, reqparse
from resources.data import BOOKINGS

class BookingList(Resource):
    def get(self):
        return BOOKINGS

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
        booking_id = int(max(BOOKINGS.keys())) + 1
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