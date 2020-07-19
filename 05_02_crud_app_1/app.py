from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
import sys
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://user1@localhost:5432/todoapp'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

#create todo model
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable = False)
    # non-nullables will cause errors when upgrading with flask migrate
    # with tables that have existing data.
    # fix this with adding steps to migration file
    completed = db.Column(db.Boolean, nullable = False, default = False)

    def __refr__(self):
        return f'<Todo {self.id} {self.description}>'

# will be managed with migrations
# db.create_all()

@app.route('/todos/create', methods=['POST'])
def create_todo():
    #lecture 5.8
    error = False
    #use dummy dict 'body' to capture todo data before it expires
    body = {}
    try:
        description = request.get_json()['description']
        todo = Todo(description = description)
        
        #testing error handling
        # todo = Todo(description2 = description)
        
        db.session.add(todo)
        db.session.commit()
        body['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    
    if not error:
        # return jsonify({
        #     'description': todo.description
        # })

        return jsonify(body)
    else:
        abort (500)


@app.route('/')
def index():
    # return render_template('index.html', data = [{
    #     'description':'Todo 1'
    # }, {
    #     'description':'Todo 2'
    # }, {
    #     'description':'Todo 8'
    # }])

    return render_template('index.html', data = Todo.query.all())
