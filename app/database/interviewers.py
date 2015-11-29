from app.models.interviewer import Interviewer


def create_interviewer(name, availabilities):
    new_interviewer = Interviewer(name=name, availabilities=availabilities,
                                  rc_id=rc_id)
    new_interviewer.save()


def get_interviewers():
    return Interviewer.objects
