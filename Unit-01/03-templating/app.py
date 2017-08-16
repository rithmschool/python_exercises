from flask import Flask, render_template
app = Flask(__name__)

@app.route('/person/<name>/<int:age>')
def show_info(name, age):
    return render_template('index.html', name=name, age=age)

if __name__ == "__main__":
    app.run(port=3000, debug=True)
