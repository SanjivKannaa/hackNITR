import sqlite3
import pickle
from flask import Flask
app = Flask(__name__)

mydb = sqlite3.connect(database="database.db", check_same_thread=False)
mycursor = mydb.cursor()




@app.route('/')
def index():
    return {
		"name": "sanjiv",
		"rollno": "106121116"
	}


app.run(host='0.0.0.0', port=81)
