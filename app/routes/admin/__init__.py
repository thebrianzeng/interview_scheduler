import copy
from pprint import pprint

from flask import Blueprint, request, redirect, render_template, session

admin = Blueprint('admin', __name__)

@admin.route('/')
def home():
    return render_template('admin_home.html')


@admin.route('/create_recruiting_cycle', methods=['POST'])
def create_recruiting_cycle():
    # create a new recruiting cycle and return the page for it
    new_recruiting_cycle_id = "1"
    new_recruiting_cycle_url = '/recruiting_cycles/' + new_recruiting_cycle_id
    return redirect(new_recruiting_cycle_url)

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
