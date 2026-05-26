from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:123@DESKTOP-SUWOFVS/danhsachABS?driver=SQL+Server'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stt = db.Column(db.Integer)
    ma_nv = db.Column(db.String(80))
    hoten = db.Column(db.String(80))
    email = db.Column(db.String(80))
    chucdanh = db.Column(db.String(80))
    donvi1 = db.Column(db.String(80))
    donvi2 = db.Column(db.String(80))
    sodienthoai = db.Column(db.String(20))
    nguoiquanly = db.Column(db.String(80))

@app.route('/dstaikhoan')
def dstaikhoan():
    users = User.query.all()
    return render_template('dstaikhoan.html', users=users)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)