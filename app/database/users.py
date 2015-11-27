from app.models.users import User


def create_user(email):
    new_user = User(email=email)
    new_user.save()


def get_user():
    pass


def get_users():
    return User.objects
