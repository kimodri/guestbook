from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# do some configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guestbook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app) # what does ths do, why do I need to pass my app?? my App is an object so is SQLAlchemy a function?

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))

# All we need to do is to create an object of this comments class by supplying the name and the comment when creating an object 


# route is the place that I can type in my browser
# it's www.flask.app/something (but this is just an http request)

@app.route('/')
def index():
    # Query all records from the Comments table
    results = Comments.query.all()

    # Pass them to the template
    return render_template('index.html', results=results)

@app.route('/sign')
def sign():
    return render_template('sign.html')

@app.route('/process', methods = ['POST', 'GET'])
def process():
    name = request.form['name']
    comment = request.form['comment']

    signature = Comments(name = name, comment = comment)
    db.session.add(signature)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

# # This is for variable lesson
# @app.route('/home/<place>', methods = ['POST'])
# def home(place):
#     return 'You are on the ' + place + ' :)'

# A lesson for loops
# @app.route('/body')
# def body():
#     links = ['https://www.youtube.com', 'https://www.python.org']
#     return render_template('example.html', links = links)


