import os	


from flask import Flask
from flask_restful import Api



from resources.cennet import Cennet, CennetList
from resources.room import Room, RoomList
from resources.button import Button, ButtonList


base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'fgnoignvoghorihgnonvznn874fiv98u'
api = Api(app)

api.add_resource(Room, '/rooms/<int:id>')
api.add_resource(RoomList, '/rooms')
api.add_resource(Button, '/buttons/<int:id>')
api.add_resource(ButtonList, '/buttons')
api.add_resource(Cennet, '/cennets/<int:id>')
api.add_resource(CennetList, '/cennets')


if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(debug=True)