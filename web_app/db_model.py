
# web_app/db_model.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    follower_count = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.username
    

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Unicode(300))
    user = db.relationship('User', backref=db.backref('text', lazy=True))

    def __repr__(self):
        return "<Tweet %r>" % self.text  

#def parse_records(database_records):
#    parsed_records = []
#    for record in database_records:
#        print(record)
#        parsed_record = record.__dict__
#        del parsed_record["_sa_instance_state"]
#        parsed_records.append(parsed_record)
#    return parsed_records