from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return("Chimmu welcome to my 1st Python web application, deployed on Heroku Cloud Platform")

if __name__ == "__main__":
    app.run()


