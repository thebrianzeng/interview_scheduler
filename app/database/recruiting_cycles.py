from app.models.recruiting_cycles import RecruitingCycle


def new_recruiting_cycle(url):
    new_recruiting_cycle = RecruitingCycle(url=url)
    new_recruiting_cycle.save()


def get_recruiting_cycle(url):
    return RecruitingCycle.objects(url=url).first()

