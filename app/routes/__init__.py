from app.routes.admin import admin
from app.routes.recruiting_cycles import rc as recruiting_cycles

def register_blueprints(app):
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(recruiting_cycles, url_prefix='/recruiting_cycles')
