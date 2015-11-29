import json

from flask import Blueprint, request, redirect, render_template, session

from app.database import interviewees as interviewees_db
from app.database import interviewers as interviewers_db


rc = Blueprint('recruiting_cycles', __name__)


@rc.route('/<rc_id>')
def get_rc_page(rc_id):
    return render_template('recruiting_cycle.html')


def get_time_slots(start_time, end_time):
    """ Both times are hours (e.g. start_time=9 means 9am) """
    time_slots = []

    cur_time = start_time
    while cur_time < end_time:
        if cur_time % 1 != 0:
            time_slot = "{cur_time}:30-{cur_time_plus_one}:00".format(
                    cur_time=str(int(cur_time)), cur_time_plus_one=str(int(cur_time) + 1))
        else:
            time_slot = "{cur_time}:00-{cur_time}:30".format(cur_time=str(int(cur_time)))

        time_slots.append(time_slot)
        cur_time += .5

    return time_slots


@rc.route('/<rc_id>/interviewee_form', methods=['GET', 'POST'])
def get_interviewee_form(rc_id):
    if request.method == 'GET':
        days = ['12/5', '12/6', '12/7', '12/8', '12/9', '12/10']
        time_slots = get_time_slots(9, 23)
        return render_template('interviewee_form.html', 
                                days=days, time_slots=time_slots)
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
