from flask import Flask,render_template,request,redirect,url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = True
db = SQLAlchemy(app)

class Comments(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(20),nullable=False)
    comment = db.Column(db.String(20),nullable=False)
    posted = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

@app.route("/")
def index():
    result  = Comments.query.all()
    return render_template('index.html',result=result)

@app.route('/process',methods=['POST'])
def process():
    name = request.form["name"]
    comment = request.form["comment"]
    posted = datetime.today()

    signature = Comments(name=name,comment=comment,posted=posted)
    db.session.add(signature)
    db.session.commit()

    return redirect(url_for('index'))
    

if __name__=="__main__":
    app.run(debug=True, port=5000)
