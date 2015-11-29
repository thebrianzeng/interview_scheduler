from app.models.interviewer import Interviewer


def create_interviewer(name, slots):
    # TODO: convert slots to a list form
    new_interviewer = User(name=name, slots=slots)
    new_interviewer.save()


def get_interviewers():
    return Interviewer.objects
