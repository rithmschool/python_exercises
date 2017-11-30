from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Unit 1, Ex 3, Part 1!"


@app.route('/person/<string>/<int:num>')
def person(string,num):
  return render_template('person.html', string=string, num=num)

if __name__ == '__main__':
  app.run(debug=True, port=3000)