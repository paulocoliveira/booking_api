from flask_restful import Resource, reqparse, request
from resources.data import BOOKINGS
import json

class BookingList(Resource):

    def get(self):
        return {'bookings': BOOKINGS}, 200


class Booking(Resource):
    
    def post(self):
        request_data = request.get_json()
        
        if next(filter(lambda x: x['first_name'] == request_data['first_name'], BOOKINGS), None):
            return {'message': "Booking with first name '{}' already exists".format(request_data['first_name'])}, 400
        
        new_booking = {
            'first_name': request_data['first_name'],
            'last_name': request_data['last_name'],
            'total_price': request_data['total_price'],
            'already_paid': request_data['already_paid'],
            'checkin': request_data['checkin'],
            'checkout': request_data['checkout'],
            'additional_needs': request_data['additional_needs']
        }
        
        BOOKINGS.append(new_booking)
        return new_booking, 201
    
    def put(self, first_name):
        request_data = request.get_json()

        item = next(filter(lambda x: x['first_name'] == first_name, BOOKINGS), None);
        if item:
            new_booking = {
                'first_name': request_data['first_name'],
                'last_name': request_data['last_name'],
                'total_price': request_data['total_price'],
                'already_paid': request_data['already_paid'],
                'checkin': request_data['checkin'],
                'checkout': request_data['checkout'],
                'additional_needs': request_data['additional_needs']
            }
            item.update(new_booking)
            return new_booking, 200
        else:
            return {'message': "Booking with first name '{}' does not exist!".format(request_data['first_name'])}, 400

    def get(self, first_name):
        booking = next(filter(lambda x: x['first_name'] == first_name, BOOKINGS), None)
        return {'booking': booking}, 200 if booking else 404
    
    def delete(self, first_name):
        global BOOKINGS
        BOOKINGS = list(filter(lambda x: x['first_name'] != first_name, BOOKINGS))
        return {'message': 'Booking deleted!'}, 200