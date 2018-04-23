from . import db

#...

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(200),unique=True)
    username=db.Column(db.String(200),unique=True)
    password_hash = db.Column(db.String(200))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
