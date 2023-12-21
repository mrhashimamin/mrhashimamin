from flask import Flask,render_template

Img_Editor=Flask(__name__)

@Img_Editor.route("/")
def homepage():
    return render_template("home.html",page_title="Home")

@Img_Editor.route("/signup")
def signuppage():
    return render_template("signup.html",page_title="Sign-Up")

@Img_Editor.route("/app")
def app():
    return render_template("app.html",page_title="App")

@Img_Editor.route("/login")
def login():
    return render_template("login.html",page_title="Log in")

if __name__=="__main__":
    Img_Editor.run(debug=True,port=9000)