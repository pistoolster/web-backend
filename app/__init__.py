from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flasgger import Swagger
from flask_restplus import Resource, Api
from flask_cors import CORS


application = Flask(__name__)
CORS(application, supports_credentials=True)

swagger = Swagger(application)

application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
login = LoginManager(application)

api = Api(application, version='1.0', title='HuXin API',
    description='Huxin API v1', doc='/doc/'
)

from app import models
from app import auth_api
from app import complaint_api
from app import merchant_query_api
