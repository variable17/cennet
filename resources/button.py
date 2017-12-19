from flask import request, jsonify, make_response
from flask_restful import Resource
from models.models import *

from db import db


class Button(Resource):
	def get(self, id):
		button = Buttons.query.filter_by(id=id).first()
		if button is None:
			return make_response(jsonify({'msg': 'No button by this id'}), 404)
		return make_response(jsonify(button.json()), 200)


	def put(self, id):
		button = Buttons.query.filter_by(id=id).first()
		if button is None:
			return make_response(jsonify({'msg': 'No button by this id'}), 404)
		data = request.get_json()
		name = data.get('name')
		power = data.get('power')
		intensity = data.get('intensity')
		rd_id = data.get('relay_id')
		if rd_id is None:
			rd_id = data.get('dimmer_id')
		button.name = name if name else button.name
		button.power = power
		button.intensity = intensity if intensity else button.intensity
		db.session.add(button)
		db.session.commit()
		if button.button_type == 'relay':
			relay = Relays.query.filter_by(relay_id=rd_id).first()
			relay.power = power
			db.session.add(relay)
			db.session.commit()
			return make_response(jsonify({'msg': 'Value changed'}), 200)
		else:
			dimmer = Dimmers.query.filter_by(dimmer_id=rd_id).first()
			dimmer.power = power
			dimmer.intensity = intensity
			db.session.add(dimmer)
			db.session.commit()
			return make_response(jsonify({'msg': 'Value changed'}), 200)
			

	def delete(self, id):
		button = Buttons.query.filter_by(id=id).first()
		if button is None:
			return make_response(jsonify({'msg': 'Button does not exists'}), 404)
		db.session.delete(button)
		db.session.commit()
		return make_response(jsonify({'msg': 'Button deleted'}), 200)



class ButtonList(Resource):
	def get(self):
		return make_response(jsonify({'buttons': [button.json() for button in Buttons.query.all()]}), 200)


	def post(self):
		data = request.get_json()
		name = data.get('name')
		button_type = data.get('button_type')
		room_id = data.get('room_id')
		power = data.get('power')
		intensity = data.get('intensity')
		ip_address = data.get('ip_address')
		rd_id = data.get('relay_id')
		if rd_id is None:
			rd_id = data.get('dimmer_id')
		button = Buttons.query.filter_by(name=name, button_type=button_type, room_id=room_id).first()
		if button is not None:
			return make_response(jsonify({'msg': 'Button already exists'}), 404)
		if button_type == 'relay':
			button = Buttons(name=name, button_type=button_type, room_id=room_id, power=power, rd_id=rd_id, ip_address=ip_address)
			db.session.add(button)
			db.session.commit()
			return make_response(jsonify({'msg': 'Button added'}), 201)
		button = Buttons(name=name, button_type=button_type, room_id=room_id, power=power, intensity=intensity ,rd_id=rd_id, ip_address=ip_address)
		db.session.add(button)
		db.session.commit()
		return make_response(jsonify({'msg': 'Button added'}), 201)	