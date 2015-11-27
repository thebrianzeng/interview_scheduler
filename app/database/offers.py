from app.models.offers import Offer


def create_offer(salary, company, 
                 has_corporate_housing, housing, 
                 relocation, perks,
                 school, graduation_year):
    new_offer = Offer(salary=salary,
                     company=company,
                     has_corporate_housing=has_corporate_housing,
                     housing=housing,
                     relocation=relocation,
                     perks=perks,
                     school=school,
                     graduation_year=graduation_year)
    new_offer.save()


def get_offer():
    pass


def get_offers():
    return Offer.objects
