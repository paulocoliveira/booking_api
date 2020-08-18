from flask import Flask, jsonify, request
from resources.data import BOOKINGS

app = Flask(__name__)

@app.route('/booking', methods=["POST"])
def create_booking():
    print("entrou no create")
    request_data = request.get_json()
    print("pegou o request data")
    new_booking = {
        'first_name': request_data['first_name'],
        'last_name': request_data['last_name'],
        'total_price': request_data['total_price'],
        'already_paid': request_data['already_paid'],
        'checkin': request_data['checkin'],
        'checkout': request_data['checkout'],
        'additional_needs': request_data['additional_needs']
    }
    print("montou o dicionário")
    BOOKINGS.append(new_booking)
    print("adicionou o dicionário na lista")
    return jsonify(new_booking)

@app.route('/booking', methods=["GET"])
def get_bookings():
    return jsonify({'bookings': BOOKINGS})

@app.route('/booking/<string:first_name>', methods=["GET"])
def get_booking_by_id(first_name):
    for book in BOOKINGS:
        if book['first_name'] == first_name:
            return jsonify(book)
    return jsonify({'message': 'Booking not found!'})

@app.route('/booking/<string:first_name>', methods=["PUT"])
def edit_booking(first_name):
    request_data = request.get_json()
    new_booking = {
        'first_name': request_data['first_name'],
        'last_name': request_data['last_name'],
        'total_price': request_data['total_price'],
        'already_paid': request_data['already_paid'],
        'checkin': request_data['checkin'],
        'checkout': request_data['checkout'],
        'additional_needs': request_data['additional_needs']
    }

    for book in BOOKINGS:
        if book['first_name'] == first_name:
            book.update(new_booking)
            return jsonify(new_booking)
    return jsonify({'message': 'Booking not found!'})

@app.route('/booking/<string:first_name>', methods=["DELETE"])
def delete_booking(first_name):
    for book in BOOKINGS:
        if book['first_name'] == first_name:
            BOOKINGS.remove(book)
    return jsonify({'message': 'Booking not found!'})


app.run()