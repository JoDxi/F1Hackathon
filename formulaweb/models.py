from formulaweb import db


class User(db.Model):
	id = db.Column(db.Integer(), primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"User('{self.username}, {self.email}')"


class Teams(db.Model):
	team_name = db.Column(db.String(50), primary_key=True, unique=True, nullable=False)
	team_boss = db.Column(db.String(50), unique=True, nullable=False)
	team_drivers = db.Column(db.String(50), nullable=False)
	team_wins = db.Column(db.Integer())
	team_description = db.Column(db.String(250), nullable=False)

	def __repr__(self):
		return f"('{self.team_name}, Team Boss - {self.team_boss}, Team Drivers- {self.team_drivers}, won {self.team_wins} World championships. {self.team_description})"