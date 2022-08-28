from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from werkzeug.utils import secure_filename

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:lamentation@localhost/soundup'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Upload(db.Model):
    id = Column(Integer, primary_key=True)
    filename = Column(String(100), unique=True, )

    def __repr__(self):
        return self.Filename


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/music', methods=['POST', 'GET'])
def music():
    if request.method == 'POST':
        file = request.files['uploads']
        file.save(f'{file.filename}')

        instant = Upload(filename=f'(secure_filename{file.filename})')
        db.session.add(instant)
        db.session.commit()

    return render_template("upload_music.html")


if __name__ == '__main__':
    app.run(
        debug=True
    )
