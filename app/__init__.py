from flask import Flask, redirect, render_template, request, session
from flask.ext.mongoengine import MongoEngine
import httplib2
import json
from oauth2client.client import OAuth2WebServerFlow

app = Flask(__name__)
db = MongoEngine(app)

from config import flask_config

from app.database import users as users_db
from models.users import User
from routes import register_blueprints
from routes.offers import get_offers

# Load config
app.config.from_object(flask_config)

# TODO: Load MongoDB config

# Register Blueprints
register_blueprints(app)

if app.debug:
    OAUTH_REDIRECT_URI = 'http://localhost:5001/oauth2callback'
else:
    OAUTH_REDIRECT_URI = 'http://salaries.thebrianzeng.com/oauth2callback' # TODO: switch

SCOPES = 'https://www.googleapis.com/auth/userinfo.email'
CLIENT_ID = app.config['CLIENT_ID']
CLIENT_SECRET = app.config['CLIENT_SECRET']


@app.route('/')
def home():
    return get_offers()

def create_flow():
    global flow
    flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
                               client_secret=CLIENT_SECRET,
                               scope=SCOPES,
                               redirect_uri=OAUTH_REDIRECT_URI)


def get_auth_uri():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    return flow.step1_get_authorize_url()


def create_user(email):
    user = User(email=email)
    user.save()
    return user


def get_user(email):
    user = User.objects.filter(email=email).first()
    print user
    return user

@app.route('/logout')
def logout():
    session.pop('email')
    return redirect('/')


@app.route('/oauth')
def oauth():
    create_flow()
    auth_uri = get_auth_uri()
    return redirect(auth_uri)


@app.route('/oauth2callback')
def oauth2callback():
    code = request.args.get('code')
    credentials = flow.step2_exchange(code)
    http = httplib2.Http()
    http = credentials.authorize(http)
    resp, content = http.request(
        'https://www.googleapis.com/oauth2/v1/userinfo?alt=json', 'GET')
    response_data = json.loads(content)
    email = response_data['email']

    user = get_user(email)
    if not user:
        user = users_db.create_user(email)

    session['email'] = user.email

    if 'return_to_create' in session:
        user_path = '/offers/create'
        session.pop('return_to_create')
    else:
        user_path = '/'

    return redirect(user_path)
