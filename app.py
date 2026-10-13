from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Halo! Aplikasi Flask dengan Database SQLite + Docker + Jenkins Berhasil Berjalan!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
