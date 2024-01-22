from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    id= db.Column(db.String(20))
    gender=db.Column(db.String(10))
    age = db.Column(db.Integer)

    emo1_happiness = db.Column(db.Integer)
    emo1_joy = db.Column(db.Integer)
    emo1_despair = db.Column(db.Integer)
    emo1_sadness = db.Column(db.Integer)
    emo1_irritation = db.Column(db.Integer)
    emo1_rage = db.Column(db.Integer)

    feedback = db.Column(db.String(400))