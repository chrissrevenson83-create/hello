from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mssql+pyodbc://sa:123@DESKTOP-SUWOFVS/danhsachABS'
    '?driver=SQL+Server&TrustServerCertificate=yes'
)
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'danhsachABS'
    __table_args__ = {'schema': 'dbo', 'extend_existing': True}

    stt = db.Column(db.SmallInteger, primary_key=True)  # tinyint, là primary key
    ma_nv = db.Column(db.String(80))
    hoten = db.Column(db.String(80))
    email = db.Column(db.String(80))
    chucdanh = db.Column(db.String(80))
    donvi1 = db.Column(db.String(80))
    donvi2 = db.Column(db.String(80))
    sodienthoai = db.Column(db.Integer)  # int
    nguoiquanly = db.Column(db.String(80))

@app.route('/dstaikhoan')
def dstaikhoan():
    try:
        users = User.query.all()
        print(f"✅ Số records: {len(users)}")
        return render_template('dstaikhoan.html', users=users)
    except Exception as e:
        return f"<h2>Lỗi:</h2><pre>{str(e)}</pre>"

if __name__ == '__main__':
    app.run(debug=True)