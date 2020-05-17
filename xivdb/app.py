

from flask import Flask
from xivdb.general.routes import general_bp
from xivdb.admin.routes import admin_bp
from xivdb.weapons.routes import weapon_bp
from xivdb.api.api import api_bp
from xivdb.api.apiWeapons import apiWeapons_bp
from xivdb.api.parse import parse_bp
from xivdb.api.jobs import apiJobs_bp

app = Flask(__name__
    ,static_folder='static'
    ,template_folder='templates')

app.register_blueprint(general_bp)
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(apiJobs_bp, url_prefix='/api/jobs')
app.register_blueprint(apiWeapons_bp, url_prefix='/api/weapons')
app.register_blueprint(parse_bp, url_prefix='/api/parse')

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(weapon_bp, url_prefix='/weapons')

