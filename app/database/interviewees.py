from app.models.interviewee import Interviewee


def create_interviewee(name, availabilities):
    new_interviewee = User(name=name, availabilities=availabilities)
    new_interviewee.save()


def get_interviewees():
    return Interviewee.objects
