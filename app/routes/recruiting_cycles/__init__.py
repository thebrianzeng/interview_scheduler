from flask import Blueprint, request, redirect, render_template, session

rc = Blueprint('recruiting_cycles', __name__)


@rc.route('/<rc_id>')
def get_rc_page(rc_id):
    return render_template('recruiting_cycle.html')


@rc.route('/<rc_id>/interviewee_form', methods=['GET', 'POST'])
def get_interviewee_form(rc_id):
    if request.method == 'GET':
        return render_template('interviewee_form.html')
    else: # POST
        pass


@rc.route('/<rc_id>/interviewer_form', methods=['GET', 'POST'])
def get_interviewer_form(rc_id):
    if request.method == 'GET':
        return render_template('interviewer_form.html')
    else: # POST
        name = request.form['name']
        print request.get_json()

        # insert into DB
        pass
