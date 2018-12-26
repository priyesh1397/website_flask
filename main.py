from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/codingthunder'
db = SQLAlchemy(app)

                            # ADDING SQL QUERY FOR CONTACT
class Contacts(db.Model):

    Sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12),nullable=False)
    message = db.Column(db.String(120),nullable=False)
    date = db.Column(db.String(12),nullable=True)
    email = db.Column(db.String(20), nullable=False)

                # HOME
@app.route("/")
def home():
    return render_template("index.html")

                # ABOUT
@app.route("/about")
def about():
    return render_template("about.html")

                # SAMPLE POST
@app.route("/post")
def post():
    return render_template("post.html")

                # CONTACT
@app.route("/contact",methods=['GET','POST'])
def contact():
    if (request.method=='POST'):
        '''ADDING DATA TO DATABASE'''
        name=request.form.get('name')
        phone=request.form.get('phone')
        mssge=request.form.get('msg')
        email=request.form.get('email')

        entry=Contacts(name=name,phone_num=phone,message=mssge,date=datetime.now(),email=email)
        db.session.add(entry)
        db.session.commit()
    return render_template("contact.html")

app.run(debug=True)