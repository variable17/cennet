from flask import request, jsonify, make_response
from flask_restful import Resource
from models.models import Rooms, Buttons, Cennets, Relays, Dimmers

from db import db


class Cennet(Resource):
	def get(self, id):
		cennet = Cennets.query.filter_by(id=id).first()
		if cennet is None:
			return make_response(jsonify({'msg': 'No such cennet'}), 404)
		return make_response(jsonify({'id': cennet.id, 'udid': cennet.udid, 'ip_address': cennet.ip_address if cennet.ip_address else 'not_set', 'name': cennet.name, 'cennet_type': cennet.cennet_type, 'discovered': cennet.discovered ,'room_id': cennet.room_id, \
		'relays': [relay.json() for relay in Relays.query.filter_by(cennet_id=cennet.id).all()], 'dimmers': [dimmer.json() for dimmer in Dimmers.query.filter_by(cennet_id=cennet.id).all()]}), 200)


	def put(self, id):
		cennet = Cennets.query.filter_by(id=id).first()
		if cennet:
			data = request.get_json()
			room_id = data.get('room_id')
			cennet.room_id = room_id
			db.session.add(cennet)
			db.session.commit()
			return make_response(jsonify({'msg':'room_id updated'}), 200)
		else:
			return make_response(jsonify({'msg': 'No cennet at this id'}), 404)


	def delete(self, id):
		cennet = Cennets.query.filter_by(id=id).first()
		if cennet is None:
			return make_response(jsonify({'msg': 'No such cennet'}), 404)
		db.session.delete(cennet)
		db.session.commit()
		return make_response(jsonify({'msg': 'cennet deleted'}), 200)



class CennetList(Resource):
	def get(self):
		return make_response(jsonify({'cennets': [cennet.json() for cennet in Cennets.query.all()]}), 200)
		
	def post(self):
		data = request.get_json()
		udid = data.get('udid')
		name = data.get('name')
		cennet_type = data.get('cennet_type')
		ip_address = data.get('ip_address')
		room_id = data.get('room_id')
		relays = data.get('relays')
		dimmers = data.get('dimmers')
		discovered = True
		cennet = Cennets.query.filter_by(udid=udid).first()
		if cennet is None:
			if room_id:
				cennet = Cennets(udid=udid, name=name, cennet_type=cennet_type, ip_address=ip_address, room_id=room_id, discovered=discovered)
			else:
				cennet = Cennets(udid=udid, name=name, cennet_type=cennet_type, ip_address=ip_address, discovered=discovered)
			db.session.add(cennet)
			db.session.commit()
			if len(relays) > 0:
				for i in relays:
					relay = Relays(cennet_id=cennet.id, power=i.get('power'), number=i.get('number'))
					db.session.add(relay)
					db.session.commit()
			if len(dimmers) > 0:
				for i in dimmers:
					dimmer = Dimmers(cennet_id=cennet.id, power=i.get('power'), intensity=i.get('intensity'), number=i.get('number'))
					db.session.add(dimmer)
					db.session.commit()
			return make_response(jsonify({'msg': 'cennet added'}), 201)
		else:
			cennet.ip_address = ip_address
			db.session.add(cennet)
			db.session.commit()
			if len(relays) > 0:
				for i, j in zip(relays, Relays.query.filter_by(cennet_id=cennet.id).all()):
					j.power = i.get('power')
					db.session.add(j)
					db.session.commit()
					button = Buttons.query.filter_by(rd_id=j.relay_id, button_type='relay').first()
					if button:
						button.power = i.get('power')
						button.ip_address = ip_address
						db.session.add(button)
						db.session.commit()
			if len(dimmers) > 0:
				for i, j in zip(dimmers, Dimmers.query.filter_by(cennet_id=cennet.id).all()):
					j.power = i.get('power')
					j.intensity = i.get('intensity')
					db.session.add(j)
					db.session.commit()
					button = Buttons.query.filter_by(rd_id=j.dimmer_id, button_type='dimmer').first()
					if button:	
						button.power = i.get('power')
						button.intensity = i.get('intensity')
						button.ip_address = ip_address
						db.session.add(j)
						db.session.commit()
			return make_response(jsonify({'msg': 'cennet updated'}), 200)
