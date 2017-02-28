from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/say_my_batch/<batch>')
def say_my_batch(batch):
    return render_template('name.html', batch=batch)
