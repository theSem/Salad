from app import db 

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=False)
	phonenumber= db.Column(db.Integer, index=True, unique=True)
	location = db.Column(db.String(64), index=True, unique=False)

	def __repr__(self):
		return '<User {}>'.format(self.username)