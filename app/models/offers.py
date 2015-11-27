from app import db

class Offer(db.Document):
    salary = db.StringField()
    company = db.StringField()
    has_corporate_housing = db.StringField()
    housing = db.StringField()
    relocation = db.StringField()
    perks = db.StringField()
    school = db.StringField()
    graduation_year = db.StringField()
