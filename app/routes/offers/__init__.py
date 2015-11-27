from flask import Blueprint, request, redirect, render_template, session

from app.database import offers as offers_db


offers = Blueprint('offers', __name__)


def get_offers():
    offers = offers_db.get_offers()
    for offer in offers:
        print offer.company
    return render_template('offers.html', offers=offers)
    

@offers.route('/create', methods=['GET', 'POST'])
def create_offer():
    if request.method == 'GET':
        if 'email' not in session:
            session['return_to_create'] = True
            return redirect('/oauth')
        return render_template('offer_create.html')
    elif request.method == 'POST':
        salary = request.form['salary']
        company = request.form['company']
        has_corporate_housing = 'Yes' if 'has_corporate_housing' in request.form else 'No'
        housing = request.form['housing']
        relocation = request.form['relocation']
        perks = request.form['perks']
        school = request.form['school']
        graduation_year = request.form['graduation_year']

        offers_db.create_offer(salary=salary,
                               company=company,
                               has_corporate_housing=has_corporate_housing,
                               housing=housing,
                               relocation=relocation,
                               perks=perks,
                               school=school,
                               graduation_year=graduation_year)
        return redirect('/')


@offers.route('/<offer_id>/update')
def update_offer(offer_id):
    pass
    

@offers.route('/<offer_id>/delete')
def delete_offer(offer_id):
    pass
