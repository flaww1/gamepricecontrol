from app import db, app
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as serializer
from flask_login import UserMixin


game_genre = db.Table('game_genre',
db.Column('id_games', db.Integer, db.ForeignKey('games.id_game')),
db.Column('id_gen', db.Integer, db.ForeignKey('genres.id_gen'))
)

game_platform = db.Table('game_platform',
db.Column('id_games', db.Integer, db.ForeignKey('games.id_game')),
db.Column('id_plat', db.Integer, db.ForeignKey('platforms.id_plat'))
)


class Genres(db.Model):

    #__tablename__ = "genres"

    id_gen = db.Column(db.Integer, primary_key=True)
    name_gen = db.Column(db.String(40), index=True, unique=True)

  #	def __repr__(self):
#	return '<Genres {}>'.format(self.name_gen)


class Platforms(db.Model):

    __tablename__ = "platforms"

    id_plat = db.Column(db.Integer, primary_key=True)
    name_plat = db.Column(db.String(40), index=True, unique=True)


class User(UserMixin, db.Model):

    #__tablename__ = "user"

    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), index=True, unique=True)
    email = db.Column(db.String(50), index=True, unique=True)
    password_hash = db.Column(db.String(24))
    is_admin = db.Column(db.Boolean(1), default=False)

    # status = db.Column(db.Boolean(1))

'''
    def set_password(self, password):
	    self.password_hash = generate_password_hash(password)

    def check_password(self, password):
	return check_password_hash(self.password_hash, password)

    def get_reset_token(self, expires_secs=600):
		s = serializer(app.config['SECRET_KEY'], expires_secs)
		return s.dumps({'id_user': self.id_user}).decode('utf-8')

    @staticmethod
	def verify_reset_token(token):
		s = serializer(app.config['SECRET_KEY'])
		try:
			id_user = s.loads(token)['user_id']
		except:
			return None
		return User.query.get(id_user)

	# def __repr__(self):
	#	return '<User {}>'.format(self.email)

    @login_manager.user_loader
    def load_user(id):
    return User.query.get(int(id))
'''

class Games(db.Model):
    __tablename__ = 'games'
    id_game = db.Column(db.Integer, primary_key=True)

    game_name = db.Column(db.String(100), index=True)
    game_image = db.Column(db.String(120), index=True)
    game_preview1 = db.Column(db.String(120), index=True)
    game_preview2 = db.Column(db.String(120), index=True)
    game_preview3 = db.Column(db.String(120), index=True)
    game_description = db.Column(db.String(200), index=True)
    game_rating = db.Column(db.Integer, index=True)
    game_date = db.Column(db.Date, index=True)

    id_gen = db.relationship('Genre', secondary=game_genre, backref=db.backref('game_platforms', lazy='dynamic'))
    id_plat = db.relationship('Platform', secondary=game_platform, backref=db.backref('game_genres', lazy='dynamic'))

# def __repr__(self):
	#	return '<Games {}>'.format(self.game_name)

'''

class Status(db.Model):
	__tablename__ = 'status'
	new = db.Column(db.Boolean(1), default = True)
    active = db.Column(db.Boolean(1))
    banned = db.Column(db.Boolean(1))

# GAME COST CONTROL (GGC)
class GCC(db.Model):
	__tablename__ = 'game_cost_control'
	id_gcc = db.Column(db.Integer, primary_key=True)
	gcc_period = db.Column(db.String(50), index=True)
    ggc_date = db.Column(db.Date, index=True)

   # id_game = db.Column(db.Integer, )

class Calendar(db.Model):
    __tablename__ = 'calendar'
	id_cal = db.Column(db.Integer, primary_key=True)
    cal_date = db.Column(db.Date(100), index=True)
    cal_week = db.Column(db.Integer, index=True)
    cal_month = db.Column(db.Integer, index=True)
    cal_quarter = db.Column(db.Integer, index=True) # trimestre
    cal_half = db.Column(db.Integer, index=True) # semestre
    cal_year = db.Column(db.Integer, index=True) 

# PRICE PER PERIOD (PPP)
class PPP(db.Model):
    __tablename__ = 'price_per_period'
	 price = db.Column(db.Numeric, primary_key=True)


game_cost_calendar = db.Table('game_cost_calendar',
    db.Column('id_cal',db.Integer, db.primary_key('calendar.id_cal')),
    db.Column('id_gcc',db. Integer, db.primary_key('game_price_control.id_gcc'))
)


'''

