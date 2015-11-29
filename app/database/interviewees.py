from app.models.interviewee import Interviewee


def create_interviewee(name, slots):
    new_interviewee = User(name=name, slots=slots)
    new_interviewee.save()


def get_interviewees():
    return Interviewee.objects
