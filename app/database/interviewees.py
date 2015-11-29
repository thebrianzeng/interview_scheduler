from app.models.interviewee import Interviewee


def create_interviewee(name, availabilities, rc_id):
    new_interviewee = Interviewee(name=name, availabilities=availabilities, 
                                  rc_id=rc_id)
    new_interviewee.save()


def get_interviewees():
    return Interviewee.objects
