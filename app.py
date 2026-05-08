from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Website Usaha Digital Berjalan dengan Python Flask"

@app.route('/ulangan')
def ulangan():
    return "Halaman Ulangan TIK"

if __name__ == '__main__':
    app.run(debug=True)
