from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import sys
from flask_migrate import Migrate
import logging

logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://user1@localhost:5432/driver_veh_db'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Drivers(db.Model):
    __tablename__ = 'drivers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable = False)
    state = db.Column(db.String(2), nullable = False)
    issued = db.Column(db.Date, nullable = False)
    vehicles = db.relationship('Vehicle', backref = 'driver', lazy=True)
    
    def __refr__(self):
        return f'<driver {self.id} {self.name}>'

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable = False)
    year = db.Column(db.Integer, nullable = False)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable = False)
    
    def __refr__(self):
        return f'<vehicle {self.id} {self.driver_id}>'


# will be managed with migrations
# db.create_all()

# @app.route('/todos/create', methods=['POST'])
# def create_todo():
#     #lecture 5.8
#     error = False
#     #use dummy dict 'body' to capture todo data before it expires
#     body = {}
#     try:
#         description = request.get_json()['description']
#         todo = Todo(description = description)
        
#         db.session.add(todo)
#         db.session.commit()
#         body['description'] = todo.description

#     except:
#         error = True
#         db.session.rollback()
#         print(sys.exc_info())
#     finally:
#         db.session.close()
    
#     if not error:
#         # return jsonify({
#         #     'description': todo.description
#         # })

#         return jsonify(body)
#     else:
#         abort (500)

# @app.route('/todos/<todo_id>/kill-it', methods=['DELETE'])
# def kill_todo(todo_id):
#     try:

#         todo = Todo.query.get(todo_id)
#         # db.session.delete(todo)
#         Todo.query.filter_by(id=todo_id).delete()
#         db.session.commit()

#     except:
#         db.session.rollback()
#     finally:
#         db.session.close()
#     return jsonify({ 'success': True })

# @app.route('/todos/<todo_id>/set-completed', methods=['POST'])
# def set_completed_todo(todo_id):
#     try:
#         completed = request.get_json()['completed']
#         print('completed', completed)
#         todo = Todo.query.get(todo_id)
#         todo.completed = completed
#         db.session.commit()

#     except:
#         db.session.rollback()
#     finally:
#         db.session.close()
#     return redirect(url_for('index'))

# @app.route('/')
# def index():
#     # return render_template('index.html', data = [{
#     #     'description':'Todo 1'
#     # }, {
#     #     'description':'Todo 2'
#     # }, {
#     #     'description':'Todo 8'
#     # }])

#     return render_template('index.html', data = Todo.query.order_by('id').all())
