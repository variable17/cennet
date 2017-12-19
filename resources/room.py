from flask import request, jsonify, make_response
from flask_restful import Resource
from models.models import Rooms, Cennets, Buttons, Relays, Buttons, Dimmers

from db import db

class Room(Resource):

	def get(self, id):
		buttons = Buttons.query.filter_by(room_id=id).all()
		if len(buttons) > 0:
			btn = []
			for button in buttons:
				btn.append(button.json())
			return make_response(jsonify({'room_id': id, 'room_name': button.room.name, 'buttons': btn}), 200)
		return make_response(jsonify({'msg': 'The room is not defined' }))


	def put(self, id):
		room = Rooms.query.filter_by(id=id).first()
		if room is None:
			return make_response(jsonify({'msg': 'Room does not exist'}), 404)
		data = request.get_json()
		name = data.get('name')
		room.name = name
		db.session.add(room)
		db.session.commit()
		return make_response(jsonify({'msg': 'Room name has changed'}), 200)

	def delete(self, id):
		room = Rooms.query.filter_by(id=id).first()
		if room is None:
			return make_response(jsonify({'msg': 'No room to begin with'}), 404)
		db.session.delete(room)
		db.session.commit()
		return make_response(jsonify({'msg': 'Room deleted'}), 200)

class RoomList(Resource):
	def get(self):
		return make_response(jsonify({'rooms': [room.json() for room in Rooms.query.all()]}), 200)

	def post(self):
		data = request.get_json()
		name = data.get('name')		
		room = Rooms(name=name)
		db.session.add(room)
		db.session.commit()
		return make_response(jsonify({'msg': 'Room added'}), 201)
		