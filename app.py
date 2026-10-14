import os
import requests
import random
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import login_required

app = Flask(__name__)
db = SQL("sqlite:///memegenerator.db")

app.secret_key = os.urandom(24)


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if not request.form.get("username"):
            flash("must provide username")
            return render_template("login.html")

        elif not request.form.get("password"):
            flash("must provide password")
            return render_template("login.html")

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["password"], request.form.get("password")
        ):
            flash("invalid username and/or password")
            return render_template("login.html")

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        if username == "":
            flash("what are you? a ghost? (Username can't be empty)")
            return render_template("register.html")
        if db.execute("SELECT * FROM users WHERE username = ?", username):
            flash("Username already exists")
            return render_template("register.html")
        if password == "" or confirmation == "":
            flash("Password can't be blank silly")
            return render_template("register.html")
        if password != confirmation:
            flash("Confirmation Password and Password are not match")
            return render_template("register.html")

        hashedPassword = generate_password_hash(password)
        new_user_id = db.execute(
            "INSERT INTO users(username, password) VALUES(?, ?)",
            username,
            hashedPassword,
        )

        session["user_id"] = new_user_id
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/meme", methods=["GET", "POST"])
@login_required
def meme():
    if request.method == "POST":
        topText = request.form.get("topText")
        bottomText = request.form.get("bottomText")
        if not topText and not bottomText:
            flash("bro tryna to generate just a image 💀 (Add at least 1 text)")
            return render_template("index.html")
        response = requests.get("https://api.imgflip.com/get_memes")
        datas = response.json()
        if datas["success"]:
            memes = datas["data"]["memes"]

            random_meme = random.choice(memes)

            random_meme_url = random_meme["url"]
        else:
            flash("please try again lol")
            return render_template("index.html")
        return render_template(
            "meme.html",
            topText=topText,
            bottomText=bottomText,
            meme_url=random_meme_url,
        )
    else:
        return render_template("index.html")


@app.route("/inventory", methods=["GET", "POST"])
@login_required
def inventory():
    if request.method == "POST":
        topText = request.form.get("topText")
        bottomText = request.form.get("bottomText")
        imageUrl = request.form.get("meme_url")
        id = session["user_id"]
        db.execute(
            "INSERT INTO memes(user_id, top_text, bottom_text, image_url) VALUES(?, ?, ?, ?)",
            id,
            topText,
            bottomText,
            imageUrl,
        )
        data = db.execute(
            "SELECT top_text, bottom_text, image_url FROM memes WHERE user_id = ?", id
        )
        return render_template("inventory.html", data=data)
    else:
        id = session["user_id"]
        data = db.execute(
            "SELECT top_text, bottom_text, image_url FROM memes WHERE user_id = ?", id
        )
        return render_template("inventory.html", data=data)


@app.route("/delete", methods=["GET", "POST"])
@login_required
def delete():
    if request.method == "POST":
        topText = request.form.get("topText")
        bottomText = request.form.get("bottomText")
        imageUrl = request.form.get("meme_url")
        id = session["user_id"]
        db.execute(
            "DELETE FROM memes WHERE user_id = ? AND top_text = ? AND bottom_text = ? AND image_url = ?",
            id,
            topText,
            bottomText,
            imageUrl,
        )
        data = db.execute(
            "SELECT top_text, bottom_text, image_url FROM memes WHERE user_id = ?", id
        )
        return render_template("inventory.html", data=data)
    else:
        id = session["user_id"]
        data = db.execute(
            "SELECT top_text, bottom_text, image_url FROM memes WHERE user_id = ?", id
        )
        return render_template("inventory.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
