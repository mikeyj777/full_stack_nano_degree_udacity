import os
from sqlalchemy import Column, String, Integer, Boolean, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = 'plants'
database_path = 'postgres://{}:{}@{}/{}'.format('postgres','postgres','localhost:5432', database_name)

db = SQLAlchemy()