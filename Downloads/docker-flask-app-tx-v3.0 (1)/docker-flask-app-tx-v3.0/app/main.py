from flask import Flask, render_template, request, redirect, url_for
from app.models import db, Work
from dotenv import load_dotenv
import os

# .envファイルを読み込む
load_dotenv()

# 環境変数からデータベース接続情報を取得
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

app = Flask(__name__)

# SQLAlchemy設定
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

# メモ一覧を表示
@app.route('/')
def index():
    works = Work.query.all()
    return render_template('index.html', works=works)

# メモの詳細を表示
@app.route('/work/<uuid:work_id>')
def view_work(work_id):
    work = Work.query.get_or_404(str(work_id))
    
    return render_template('view_work.html', work=work)
    

#申し込み完了を表示
@app.route('/work/apply')
def apply():
    return render_template('apply.html')

#マイページを表示
@app.route('/my_page')
def my_page():
    return render_template('my_page.html')
                           
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)