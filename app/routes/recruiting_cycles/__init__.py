import json

from flask import Blueprint, request, redirect, render_template, session, jsonify

from app.database import interviewees as interviewees_db
from app.database import interviewers as interviewers_db
from app.routes.admin import get_slots_to_interviewers


rc = Blueprint('recruiting_cycles', __name__)


@rc.route('/<rc_id>/data')
def get_rc_page(rc_id):
    interviewers = interviewers_db.get_interviewers(rc_id)
    interviewees = interviewees_db.get_interviewees(rc_id)
    return render_template('recruiting_cycle.html', interviewers=interviewers,
                            interviewees=interviewees, rc_id=rc_id)


def get_time_slots(start_time, end_time):
    """ Both times are hours (e.g. start_time=9 means 9am) """
    time_slots = []

    cur_time = start_time
    while cur_time < end_time:
        display_time = cur_time % 12 if cur_time >= 13 else cur_time
        am_pm = 'am' if cur_time < 12 else 'pm'
        if cur_time % 1 != 0:
            time_slot = "{cur_time}:30-{cur_time_plus_one}:00".format(
                cur_time=str(int(cur_time)),
                cur_time_plus_one=str(int(cur_time) + 1))
            label = ''
        else:
            time_slot = "{cur_time}:00-{cur_time}:30".format(
                cur_time=str(int(cur_time)))
            label = '{} {}'.format(str(int(display_time)), am_pm)

        time_slots.append((time_slot, label))
        cur_time += .5

    return time_slots


@rc.route('/<rc_id>/interviewee_form', methods=['GET', 'POST'])
def get_interviewee_form(rc_id):
    if request.method == 'GET':
        days = ['12/5', '12/6', '12/7', '12/8', '12/9', '12/10']
        time_slots = get_time_slots(9, 24)

        slots_to_interviewers = get_slots_to_interviewers(rc_id) 
        slots_available = set(slots_to_interviewers.keys())

        return render_template('interviewee_form.html', 
                                rc_id=rc_id, days=days, time_slots=time_slots)
    else: # POST
        name_and_availabilities = request.get_json()
        name = name_and_availabilities['name']
        availabilities = name_and_availabilities['availabilities']

        interviewees_db.create_interviewee(name=name, availabilities=availabilities, 
                                           rc_id=rc_id)
        return jsonify(data='success')


@rc.route('/<rc_id>/interviewer_form', methods=['GET', 'POST'])
def get_interviewer_form(rc_id):
    if request.method == 'GET':
        days = ['12/5', '12/6', '12/7', '12/8', '12/9', '12/10']
        time_slots = get_time_slots(9, 24)
        return render_template('interviewer_form.html', 
                                rc_id=rc_id, days=days, time_slots=time_slots)
    else: # POST
        name_and_availabilities = request.get_json()
        name = name_and_availabilities['name']
        availabilities = name_and_availabilities['availabilities']

        interviewers_db.create_interviewer(name=name, availabilities=availabilities,
                                           rc_id=rc_id)
        return jsonify(data='success')


@rc.route('/form_submitted')
def get_form_submitted_page():
    return render_template('form_submitted.html')

