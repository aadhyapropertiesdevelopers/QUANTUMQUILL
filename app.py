from flask import Flask, render_template

app = Flask(__name__)


# Route for the Home page (you can customize this as well)
@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':

    app.run(debug=True)