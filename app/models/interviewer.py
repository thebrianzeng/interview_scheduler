from app import db

class Interviewer(db.Document):
    name = db.StringField(max_length=70)
    slots = db.ListField()
