import os
import requests
import urllib.parse

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps


app = Flask(__name__)

#loading the database
db = SQL("sqlite:///rant.db")

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#this is to ensure that people who aren't registered users can't access the 'SavedQuotes' webpage
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

#this is the welcome/main page.
@app.route("/")
def rantmachine():
    return render_template("rantmachine.html")

#This converts the users' paragraph into a list of words, matches those words to the words in words.txt.
#If a match is found, it redirects the user to brainy.quote for the specific word. If no match is found,
#they are redirected to response.html which uses their name in the text found on that webpage.
@app.route("/LetItGo", methods=["GET", "POST"])
def LetItGo():
    if request.method == "POST":
        #accessing the rant paragraph
        problemtext = request.form.get("Rant")
        #matching words in words.txt to the paragraph
        with open('words.txt', 'r') as words:
            for word in words:
                for problemwords in  problemtext.split():
                    if word.lower().rstrip("\n") == problemwords.lower().rstrip("\n"):
                        link1 = "https://www.brainyquote.com/search_results?q=" + word
                        link = link1.rstrip("\n")
                        print(link)
                        #redirecting to brainyquote
                        return redirect(link)
            #redirecting to response.html
            return render_template("response.html", name=request.form.get("Name"))
    else:
        return render_template("LetItGo.html")

#This has the same exact function as /LetItGo but it is only for the logged in users.
#in addition to matching words, reidrecting to brainyquote or response.html, it saves the users quote to a
#table, "SavedQuotes" in rant.db so that they can view it some other time when they log in again
@app.route("/LetItGo2", methods=["GET", "POST"])
@login_required
def LetItGo2():
    if request.method == "POST":
        problemtext = request.form.get("Rant")
        with open('words.txt', 'r') as words:
            for word in words:
                for problemwords in  problemtext.split():
                    if word.lower().rstrip("\n") == problemwords.lower().rstrip("\n"):
                        link1 = "https://www.brainyquote.com/search_results?q=" + word
                        link = link1.rstrip("\n")
                        #saving the quote link
                        db.execute("INSERT INTO SavedQuotes (user_id, Quote) VALUES(?,?)"
                        ,session["user_id"], link)
                        return redirect(link)
            return render_template("response.html", name=request.form.get("Name"))
    else:
        return render_template("LetItGo2.html")

#logging in
@app.route("/login", methods=["GET","POST"])
def login():
    session.clear()
    #check if they input username
    if request.method == "POST":
        if not request.form.get("username"):
            return redirect("/error")
        #check if they input password
        elif not request.form.get("password"):
            return redirect("/error")
        #check if their info matches what we have in "ReturningUsers" table in rant.db
        rows = db.execute("SELECT * FROM ReturningUsers WHERE username = ?", request.form.get("username"))
        if len(rows) != 1 or not check_password_hash(rows[0]["password"], request.form.get("password")):
            return redirect("/error")
        session["user_id"] = rows[0]["id"]
        #load "SavedQuotes"
        return redirect("/SavedQuotes")
    else:
        return render_template("login.html")

#for when mistakes are made when logging in/registering
@app.route("/error")
def error():
    return render_template("error.html")

#registration for new users
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        if not request.form.get("username"):
            return redirect("/error")
        elif not request.form.get("password"):
            return redirect("/error")
        elif request.form.get("password") != request.form.get("confirmation"):
            return redirect("/error")
        try:
            #if all info is correct, the user is entered into "ReturningUsers" in rant.db
            id = db.execute("INSERT INTO ReturningUsers (username, password) VALUES(?, ?)",
                            request.form.get("username"),
                            generate_password_hash(request.form.get("password")))
        except RuntimeError:
            return redirect("/error")
        session["user_id"] = id
        return redirect("/login")
    else:
        return render_template("register.html")


@app.route("/SavedQuotes")
@login_required
def SavedQuotes():
    #load a table with savedquotes, if applicable, for logged in users
    SavedQuotes = db.execute(
        "SELECT * FROM SavedQuotes WHERE user_id = ?", session["user_id"])
    return render_template("SavedQuotes.html", SavedQuotes=SavedQuotes)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
