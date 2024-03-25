from app import db, app, login_manager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import datetime
from flask_whooshee import Whooshee
whooshee = Whooshee(app)

 



class Genres(db.Model):

    __tablename__ = "genres"

    id_gen = db.Column(db.Integer, primary_key=True)
    name_gen = db.Column(db.String(40), index=True, unique=True)
 

    def __repr__(self):
        return '<Genres {}>'.format(self.name_gen)


class Platforms(db.Model):

    __tablename__ = "platforms"

    id_plat = db.Column(db.Integer, primary_key=True)
    name_plat = db.Column(db.String(40), index=True, unique=True)
    icon_plat = db.Column(db.String(120), index=True)

    id_subplat = db.relationship('SubPlatforms', backref='platforms')

class SubPlatforms(db.Model):

    __tablename__ = "subplatforms"

    id_subplat = db.Column(db.Integer, primary_key=True)
    name_subplat = db.Column(db.String(40), index=True, unique=True)
    icon_subplat = db.Column(db.String(120), index=True)

    id_plat = db.Column(db.Integer, db.ForeignKey('platforms.id_plat'))



class User(UserMixin, db.Model):

    __tablename__ = "user"

    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), index=True, unique=True)
    email = db.Column(db.String(50), index=True, unique=True)
    password_hash = db.Column(db.Binary(60), nullable = False)
    registered_on = db.Column(db.DateTime, nullable=False)
    is_admin = db.Column(db.Boolean(1), default=False)
    remember_me = db.Column(db.Boolean(1), default=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    # status = db.Column(db.Boolean(1))
   

    @login_manager.user_loader
    def load_user(id_user):
        return User.query.get(int(id_user))
    
    def get_id(self):
        return (self.id_user)


    def __init__(self, username, email, password_hash, confirmed,
                  admin=False, confirmed_on=None):
        self.username = username         
        self.email = email
        self.password_hash = password_hash
        self.registered_on = datetime.datetime.now()
        self.is_admin = False
        self.confirmed = confirmed
        self.confirmed_on = confirmed_on
    
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'id_user': self.id_user}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            id_user = s.loads(token)['id_user']
        except:
            return None
        return User.query.get(id_user)     
  

game_genre = db.Table('game_genre',
db.Column('id_games', db.Integer, db.ForeignKey('games.id_game')),
db.Column('id_gen', db.Integer, db.ForeignKey('genres.id_gen'))
)

game_subplatform = db.Table('game_subplatform',
db.Column('id_games', db.Integer, db.ForeignKey('games.id_game')),
db.Column('id_subplat', db.Integer, db.ForeignKey('subplatforms.id_subplat'))
)

#NÃO NECESSÁRIO MAS AQUI POR PERCAUÇÃO 

game_cost_calendar = db.Table('game_cost_calendar',
    db.Column('id_cal',db.Integer, db.ForeignKey('calendar.id_cal')),
    db.Column('id_gcc',db.Integer, db.ForeignKey('game_cost_control.id_gcc')),
    db.Column('price',db.Numeric)
)


@whooshee.register_model('game_name')
class Games(db.Model):

   
    __tablename__ = 'games'
    #__searchable__ = ['game_name']
    id_game = db.Column(db.Integer, primary_key=True)

    game_name = db.Column(db.String(100), index=True)
    game_image = db.Column(db.String(120), index=True)
    game_preview1 = db.Column(db.String(120), index=True)
    game_preview2 = db.Column(db.String(120), index=True)
    game_preview3 = db.Column(db.String(120), index=True)
    game_description = db.Column(db.String(2000), index=True)
    game_rating = db.Column(db.Integer, index=True)
    game_date = db.Column(db.Date, index=True)
    game_video = db.Column(db.String(120), index=True)
    game_review = db.Column(db.String(120), index=True)

    id_gen = db.relationship('Genres', secondary=game_genre, backref=db.backref('game_genres', lazy='dynamic'))
    id_subplat = db.relationship('SubPlatforms', secondary=game_subplatform, backref=db.backref('game_subplatforms', lazy='dynamic'))    
    ggc = db.relationship('GCC', backref='games')

    def __init__(self, game_name, game_image, game_preview1, game_preview2, game_preview3, game_description, game_rating, game_date, game_video, game_review):
 
        self.game_name = game_name
        self.game_image = game_image
        self.game_preview1 = game_preview1
        self.game_preview2 = game_preview2
        self.game_preview3 = game_preview3
        self.game_description = game_description
        self.game_rating = game_rating
        self.game_date = game_date
        self.game_video = game_video
        self.game_review = game_review


'''
class Status(db.Model):
    __tablename__ = 'status'
    new = db.Column(db.Boolean(1), default = True)
    active = db.Column(db.Boolean(1))
    banned = db.Column(db.Boolean(1))
'''

# GAME COST CONTROL (GGC)
class GCC(db.Model):
    __tablename__ = 'game_cost_control'

    id_gcc = db.Column(db.Integer, primary_key=True)
    gcc_period = db.Column(db.String(50), index=True)
    gcc_date = db.Column(db.Date, index=True)
    id_game = db.Column(db.Integer, db.ForeignKey('games.id_game'))

   
class Calendar(db.Model):
    __tablename__ = 'calendar'

    id_cal = db.Column(db.Integer, primary_key=True)
    cal_date = db.Column(db.Date, index=True)
    cal_week = db.Column(db.Integer, index=True)
    cal_month = db.Column(db.Integer, index=True)
    cal_quarter = db.Column(db.Integer, index=True) # trimestre
    cal_half = db.Column(db.Integer, index=True) # semestre
    cal_year = db.Column(db.Integer, index=True) 

# PRICE PER PERIOD (PPP)








