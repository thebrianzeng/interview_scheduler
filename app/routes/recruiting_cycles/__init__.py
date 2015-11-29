import json

from flask import Blueprint, request, redirect, render_template, session

from app.database import interviewees as interviewees_db
from app.database import interviewers as interviewers_db


rc = Blueprint('recruiting_cycles', __name__)


@rc.route('/<rc_id>')
def get_rc_page(rc_id):
    return render_template('recruiting_cycle.html')


@rc.route('/<rc_id>/interviewee_form', methods=['GET', 'POST'])
def get_interviewee_form(rc_id):
    if request.method == 'GET':
        return render_template('interviewee_form.html')
    else: # POST
        availabilities = request.get_json()
        return 'success'
#        name = request.form['name']
#        name = request.slots['slots']
#
#        interviewee_db.create_interviewee(name, slots)
#
#        return render_template('interviewee_form_submitted.html')
#

@rc.route('/<rc_id>/interviewer_form', methods=['GET', 'POST'])
def get_interviewer_form(rc_id):
    if request.method == 'GET':
        return render_template('interviewer_form.html')
    else: # POST
        name = request.form['name']
        name = request.slots['slots']

        interviewer_db.create_interviewer(name, slots)

        return render_template('interviewer_form_submitted.html')
