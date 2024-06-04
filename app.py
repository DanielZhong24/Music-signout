from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("view/index.html")

@app.route('/music')
def music():
    return '<h1>This is a page for music !!!!!</h1>'

#main loop
if __name__ == '__main__':
    app.run(debug=True)
