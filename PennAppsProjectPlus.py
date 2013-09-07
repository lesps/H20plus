import os
from flask import Flask #Import flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__) #Make name of app name of main file
db = SQLAlchemy(app)

@app.route('/') #At main url
def mainPage():
  return 'Hello World!'

#Only run the app if the script is run from the main python interpreter
if __name__ == '__main__': 
  port=int(os.environ.get('PORT', 5000))
  app.run()
