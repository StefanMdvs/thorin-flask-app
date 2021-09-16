import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    # initialize an empty array and then use an with block to open 
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data) #the company argument can be named anything we want

@app.route("/about/<member_name>") #the <> will pass in the data from our url keys
def about_member(member_name): #when we look at our about url with something after it, that will be passed into this view
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj['url'] == member_name:
                member = obj
    return render_template("member.html", member=member) # first member is the variable name being passed through into our html file
                                                            # the second member is the member object created above


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template('contact.html', page_title="Contact")


@app.route("/careers")
def careers():
    return render_template('careers.html', page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)