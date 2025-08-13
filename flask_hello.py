from flask import Flask

app = Flask(__name__)

@app.get("/")
def home_page():
    return "<h1>This is the home page</h1>"

@app.get("/about")
def about_page():
    return "<h1>This is about page</h1>"

if __name__ == '__main__':
    app.run()
