from flask import Blueprint, request, render_template

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

        print (time_slot, label)
        time_slots.append((time_slot, label))
        cur_time += .5

    return time_slots


@rc.route('/<rc_id>/interviewee_form', methods=['GET', 'POST'])
def get_interviewee_form(rc_id):
    if request.method == 'GET':
        days = ['12/5', '12/6', '12/7', '12/8', '12/9', '12/10']
        time_slots = get_time_slots(9, 23)
        return render_template('interviewee_form.html',
                               days=days, time_slots=time_slots)
    else:  # POST
        name_and_availabilities = request.get_json()
        name = name_and_availabilities['name']
        availabilities = name_and_availabilities['availabilities']

        interviewees_db.create_interviewee(name=name,
                                           availabilities=availabilities)
        return 'success'


@rc.route('/<rc_id>/interviewer_form', methods=['GET', 'POST'])
def get_interviewer_form(rc_id):
    if request.method == 'GET':
        days = ['12/5', '12/6', '12/7', '12/8', '12/9', '12/10']
        time_slots = get_time_slots(9, 23)
        return render_template('interviewer_form.html',
                               days=days, time_slots=time_slots)
    else:  # POST
        name_and_availabilities = request.get_json()
        name = name_and_availabilities['name']
        availabilities = name_and_availabilities['availabilities']

        interviewers_db.create_interviewer(name=name,
                                           availabilities=availabilities)
        return 'success'
