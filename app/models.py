from datetime import datetime
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    meister_rel = db.relationship('Movie', foreign_keys="Movie.meister_id", backref='meister', lazy='dynamic')
    input_user_rel = db.relationship('Movie', foreign_keys="Movie.input_user_id", backref='input_user', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    event_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    meister_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    imbd_code = db.Column(db.String(64), index=True, unique=True)
    title = db.Column(db.String(4000), index=True, unique=True)
    year = db.Column(db.Integer, index=True, unique=True)
    length_minute = db.Column(db.Integer, index=True, unique=True)
    rating = db.Column(db.Float, index=True, unique=True)

    #meister_rel = db.relationship("User", foreign_keys="meister_id")
    #input_user_rel = db.relationship("User", foreign_keys="user_id")

    def __repr__(self):
        return '<Movie {} {} {} {} {}>'.format(self.title, self.rating, self.year, self.timestamp, self.meister_id)
