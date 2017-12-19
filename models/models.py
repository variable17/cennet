from db import db

class Rooms(db.Model):
	__tablename__ = 'rooms'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(40))
	cennets = db.relationship('Cennets', backref='value', lazy=True)
	buttons = db.relationship('Buttons', backref='room', cascade='all, delete-orphan', lazy=True)

	def json(self):
		return {'id': self.id, 'name': self.name}


class Cennets(db.Model):
	__tablename__ = 'cennets'
	id = db.Column(db.Integer, primary_key = True)
	udid = db.Column(db.String(40))
	name = db.Column(db.String(40))
	cennet_type = db.Column(db.String(40))
	discovered = db.Column(db.Boolean)
	ip_address = db.Column(db.String(25))
	room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
	relays = db.relationship('Relays', backref='cennet', cascade='all, delete-orphan', lazy=True)
	dimmers = db.relationship('Dimmers', backref='cennet', cascade='all, delete-orphan', lazy=True)

	def json(self):
		return {'id': self.id, 'udid': self.udid, 'ip_address': self.ip_address if self.ip_address else 'not_set','name': self.name, 'cennet_type': self.cennet_type, 'discovered': self.discovered ,'room_id': self.room_id}
		# 'relays': [relay.json() for relay in Relays.query.filter_by(cennet_id=self.id).all()], 'dimmers': [dimmer.json() for dimmer in Dimmers.query.filter_by(cennet_id=self.id).all()]}



class Buttons(db.Model):
	__tablename__ = 'buttons'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(40))
	button_type = db.Column(db.String(40))
	power = db.Column(db.Boolean)
	intensity = db.Column(db.Integer)
	room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'))
	rd_id = db.Column(db.Integer)
	ip_address = db.Column(db.String(40))

	def json(self):
		if self.button_type == 'dimmer':
			return {'id': self.id, 'room_id': self.room_id, 'name': self.name, 'button_type': self.button_type, 'power': self.power, 'intensity': self.intensity, 'dimmer_id': self.rd_id, 'ip_address': self.ip_address}
		else:
			return {'id': self.id,	'room_id': self.room_id, 'name': self.name, 'button_type': self.button_type, 'power': self.power, 'relay_id': self.rd_id, 'ip_address': self.ip_address}


class Relays(db.Model):
	__tablename__ = 'relays'
	relay_id = db.Column(db.Integer, primary_key = True)
	cennet_id = db.Column(db.Integer, db.ForeignKey('cennets.id'))
	number = db.Column(db.Integer)
	power = db.Column(db.Boolean)

	def json(self):
		return{'id': self.relay_id, 'power': self.power, 'number': self.number}


class Dimmers(db.Model):
	__tablename__ = 'dimmers' 
	dimmer_id = db.Column(db.Integer, primary_key = True)
	cennet_id = db.Column(db.Integer, db.ForeignKey('cennets.id'))
	power = db.Column(db.Boolean)
	number = db.Column(db.Integer)
	intensity = db.Column(db.Integer)

	def json(self):
		return{'id': self.dimmer_id, 'power': self.power, 'intensity': self.intensity, 'number': self.number}



