from app import db

class RecruitingCycle(db.Document):
    url = db.StringField(max_length=70)
