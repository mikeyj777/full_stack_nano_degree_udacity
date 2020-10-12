from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user1@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable=False, unique=True)
    #price = db.Column(db.Float, db.CheckConstraint('price>0'))

    def __repr__(self):
        #will print the ID and name fields from each queried record
        return f'<Person ID: {self.id}, name: {self.name}>'

db.create_all()

@app.route('/')
def index():
    person = Person.query.first()

    

    # person = Person(name='Amy')
    # db.session.add(person)
    # db.session.commit()

    return 'Hello ' + person.name
    #return 'Hello World'
