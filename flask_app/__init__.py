from flask import Flask

app = Flask(__name__)
app.secret_key = 'Phoenix'
DATABASE = 'basic_python_project_db'