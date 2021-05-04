from flask import *
from dotenv import load_dotenv
import os

load_dotenv()
app=Flask(__name__,static_folder='../frontend',template_folder='../frontend/views')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/spotanalyst')
def login():
    return render_template('spotanalyst.html')

if __name__ == '__main__':
    app.run(host='localhost', port=os.getenv('PORT'),debug=True)