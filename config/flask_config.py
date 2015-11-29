from sys import stderr, exit
try:
    import secrets

    # Secret Values
    SECRET_KEY = secrets.SECRET_KEY
    CLIENT_ID = secrets.CLIENT_ID
    CLIENT_SECRET = secrets.CLIENT_SECRET

    # Flask configurations
    HOST = '0.0.0.0'
    PORT = 5000
    DEBUG = True

    # Meta
    META_TITLE = 'When2Interview'
    META_DESCRIPTION = 'Fill out your interview schedule with ease!'
    META_TWITTER_HANDLE = '@adicu'
    META_DOMAIN = 'apply.adicu.com'
    SSL = False
    META_URL = ('https://' if SSL else 'http://') + META_DOMAIN
    META_IMAGE = 'img/CHANGE_ME.jpg'

except ImportError:
    print >> stderr, ('Failed to import config/secrets.py. You should copy '
                      'config/example.secrets.py into config/secets.py and '
                      'edit the values in there.')
    exit(1)
