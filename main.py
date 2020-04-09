from flask import Flask, escape, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.run('127.0.0.1', 8000)