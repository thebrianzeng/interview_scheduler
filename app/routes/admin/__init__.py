import copy
from pprint import pprint

from flask import Blueprint, request, redirect, render_template, session, jsonify

from app.database import interviewees as interviewees_db
from app.database import interviewers as interviewers_db
from app.database import recruiting_cycles as rc_db

admin = Blueprint('admin', __name__)


@admin.route('/')
def home():
    return render_template('admin_home.html')


@admin.route('/new_recruiting_cycle', methods=['GET', 'POST'])
def new_recruiting_cycle():
    if request.method == 'GET':
        return render_template('new_recruiting_cycle.html')
    else:  # POST
        url = request.form['url']
        rc_db.new_recruiting_cycle(url=url)
        return redirect(url)


@admin.route('/<rc_id>/get_schedules')
def get_schedules(rc_id):
    interviewees_to_slots = get_interviewees_to_slots(rc_id)
    slots_to_interviewers = get_slots_to_interviewers(rc_id)

    possible_schedules = match(slots_to_interviewers, interviewees_to_slots,
                               {}, [])

    return jsonify(data=possible_schedules)


def get_interviewees_to_slots(rc_id):
    interviewees_to_slots = {}

    interviewees = interviewees_db.get_interviewees(rc_id)
    for interviewee in interviewees:
        interviewees_to_slots[interviewee.name] = interviewee.availabilities

    return interviewees_to_slots


def get_slots_to_interviewers(rc_id):
    slots_to_interviewers = {}

    interviewers = interviewers_db.get_interviewers(rc_id)

    for interviewer in interviewers:
        for slot in interviewer.availabilities:
            if slot not in slots_to_interviewers:
                slots_to_interviewers[slot] = []

            slots_to_interviewers[slot].append(interviewer.name)

    return slots_to_interviewers


def match(slots_to_interviewers, interviewees_to_slots, current_schedule, possible_schedules):
    if not interviewees_to_slots:
        possible_schedules.append(current_schedule)
        return

    for interviewee, interviewee_slots in interviewees_to_slots.viewitems():
        for slot, interviewers in slots_to_interviewers.viewitems():
            if slot in interviewee_slots:
                for interviewer in interviewers:
                    interviewer_interviewee_pair = {'interviewer': interviewer,
                                                    'interviewee': interviewee}

                    new_current_schedule = copy.deepcopy(current_schedule)

                    if slot not in new_current_schedule:
                        new_current_schedule[slot] = []

                    new_current_schedule[slot].append(interviewer_interviewee_pair)

                    new_interviewees_to_slots = copy.deepcopy(interviewees_to_slots)
                    new_interviewees_to_slots.pop(interviewee)

                    new_slots_to_interviewers = copy.deepcopy(slots_to_interviewers)
                    new_slots_to_interviewers[slot].remove(interviewer)

                    match(new_slots_to_interviewers, new_interviewees_to_slots, new_current_schedule, possible_schedules)

    return possible_schedules
           

if __name__ == '__main__':
    # Test case - normal
    slots_to_interviewers = {'slot1': ['interviewer 1'],
                             'slot2': ['interviewer 2']}
                            # 'slot2': ['interviewer 1', 'interviewer 2']}
#    interviewers_to_slots = {'interviewer 1': ['slot1', 'slot2'],
#                             'interviewer 2': ['slot1', 'slot2']}
    interviewees_to_slots = {'interviewee 1': ['slot1', 'slot2'],
                             'interviewee 2': ['slot1', 'slot2']}

    result = match(slots_to_interviewers, interviewees_to_slots, {}, [])
    print '\nFinal result: '
    pprint(result)
