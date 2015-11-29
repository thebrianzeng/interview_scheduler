from app.models.interviewer import Interviewer


def create_interviewer(name, availabilities):
    new_interviewer = User(name=name, availabilities=availabilities)
    new_interviewer.save()


def get_interviewers():
    return Interviewer.objects
