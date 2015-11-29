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


def match(interviewers_to_slots, interviewees_to_slots, current_schedule, possible_schedules=[]):
    """ Generate the interview matching """
    if not interviewees_to_slots:
        possible_schedules.append(current_schedule)

    for interviewer, interviewer_slots in interviewers_to_slots.items():
        for interviewee, interviewee_slots in interviewees_to_slots.items():
            for slot in interviewee_slots:
                if slot in interviewer_slots:
                    interviewer_interviewee_pair = {'interviewer': interviewer, 
                                                    'interviewee': interviewee}

                    if slot not in current_schedule:
                        current_schedule[slot] = []

                    current_schedule[slot].append(interviewer_interviewee_pair)
                    
                    interviewees_to_slots.pop(interviewee)
                    interviewers_to_slots[interviewer].remove(slot)

                    if not interviewers_to_slots[interviewer]:
                        interviewers_to_slots.pop(interviewer)

                    current_schedule = match(interviewers_to_slots, interviewees_to_slots, current_schedule)
                    
    return possible_schedules # couldn't match them


if __name__ == '__main__':
    # Test case - normal
    interviewers_to_slots = {'interviewer 1': ['slot1', 'slot2'],
                             'interviewer 2': ['slot2', 'slot3']}
    interviewees_to_slots = {'interviewee 1': ['slot1', 'slot5'],
                             'interviewee 2': ['slot2', 'slot3']}

    print match(interviewers_to_slots, interviewees_to_slots, {})
