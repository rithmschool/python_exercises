from flask import Flask

app = Flask(__name__)

#have a route for /welcome, which responds with the string "Welcome"
@app.route('/welcome')
def welcome():
  return "welcome"

#have a route for /welcome/home, which responds with the string "Welcome home"
@app.route('/welcome/<word>')
def welcome_custom(word):
  return "welcome " + word

#Add another route to /sum and inside the function which sends a response, 
#create a variable called sum which is equal to 5+5. Respond with the sum variable.
@app.route('/sum')
def print_sum():
  sum = 5+5
  return str(sum)

if __name__ == '__main__':
  app.run(debug=True, port=4000) 

