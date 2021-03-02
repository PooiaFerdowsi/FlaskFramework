from flask import ( 
  Flask , render_template 
  request
)

app = Flask("__main__") # also can ve Flask(__name__)

@app.route('/')
def index():
  return render_template("index.htm")

@app.route('/user/<int:id>')
def profile(user:int):
  return f"Hello The User with {user} ID"

@app.route('/pooia/<float:me>')
def pooia(me:float):
  return f'{me}'

@app.route("/login",methods=['GET','POST'])
def login():
  return "<form action='/log' method='GET'><input type='text' name='pswd'/></form>"

@app.route('/log')
def log():
  return request.args.get("pswd")

if __name__ == "__main__":
  app.run(debug=True,host="0.0.0.0",port="5000")
