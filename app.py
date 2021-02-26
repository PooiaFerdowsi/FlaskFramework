from flask import ( 
  Flask , render_template )

app = Flask("__main__") # also can ve Flask(__name__)

@app.route('/')
def index():
  return render_template("index.htm")

@app.route('/user/int:<id>')
def profile(user:int):
  return f"Hello The User with {user} ID"

if __name__ == "__main__":
  app.run(debug=True,host="0.0.0.0",port="5000")
