from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        return redirect(url_for("user", name=request.form["name"]))
    return render_template("index.html")

@app.route("/contact")
def contact():
    return "<p>Don't contact me. I dont want to talk to you</p>"

@app.route("/<name>")
def user(name):
    return render_template("user.html")


if __name__ == "__main__":
    app.run(debug=True)

